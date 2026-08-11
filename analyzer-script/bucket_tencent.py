import qcloud_cos
from qcloud_cos.streambody import StreamBody
from .bucket_spec import RemoteBucket
from contextlib import contextmanager
from typing import Iterable, Optional
import logging

@contextmanager
def logger_muter(logger_name: str = 'qcloud_cos.cos_client'):
    target_logger = logging.getLogger(logger_name)
    old_level = target_logger.level
    try:
        if old_level < logging.WARNING:
            target_logger.setLevel(logging.WARNING)
        yield
    finally:
        target_logger.setLevel(old_level)

class TencentBucket(RemoteBucket):
    def __init__(self, bucket_name: str, access_key_id: str, access_key_secret: str, region: str, **kwargs):
        self.bucket_name = bucket_name
        auth_token: Optional[str] = kwargs.get('token', None)
        self.client = qcloud_cos.CosS3Client(qcloud_cos.CosConfig(
            Region=region, SecretId=access_key_id, SecretKey=access_key_secret, Token=auth_token,
            PoolMaxSize=int(kwargs.get('max_workers', 50)) + 10,
        ))

    def list_files(self, prefix: str) -> Iterable[str]:
        with logger_muter():
            marker: str = ''
            while True:
                response: dict = self.client.list_objects(Bucket=self.bucket_name, Prefix=prefix, Marker=marker, MaxKeys=1000)
                if 'Contents' in response:
                    for content in response['Contents']:
                        yield content['Key']
                if response['IsTruncated'] == 'false':
                    break
                marker = response["NextMarker"]

    def get_file_content(self, key: str) -> Iterable[bytes]:
        with logger_muter():
            result = self.client.get_object(Bucket=self.bucket_name, Key=key)
            body: StreamBody = result['Body']
            yield from body.get_stream()
    
    def delete_files(self, keys: list[str]) -> Iterable[str]:
        if len(keys) > 1000:
            raise ValueError('Key list exceeds size limit')
        with logger_muter():
            req_object = {'Quiet': 'true', 'Object': [{'Key': k} for k in keys]}
            result: dict = self.client.delete_objects(Bucket=self.bucket_name, Delete=req_object)
            return ['{}: {}'.format(e.get('Key', '???'), e.get('Message', '???')) for e in result.get('Error', ())]
