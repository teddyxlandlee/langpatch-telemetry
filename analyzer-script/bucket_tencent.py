import qcloud_cos
from qcloud_cos.streambody import StreamBody
from .bucket_spec import RemoteBucket
from typing import Iterable, Optional

class TencentBucket(RemoteBucket):
    def __init__(self, bucket_name: str, access_key_id: str, access_key_secret: str, region: str, **kwargs):
        self.bucket_name = bucket_name
        auth_token: Optional[str] = kwargs.get('token', None)
        self.client = qcloud_cos.CosS3Client(qcloud_cos.CosConfig(
            Region=region, SecretId=access_key_id, SecretKey=access_key_secret, Token=auth_token
        ))

    def list_files(self, prefix: str) -> Iterable[str]:
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
        result = self.client.get_object(Bucket=self.bucket_name, Key=key)
        body: StreamBody = result['Body']
        yield from body.get_stream()
