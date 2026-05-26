import alibabacloud_oss_v2 as _oss
from .bucket_spec import RemoteBucket
from typing import Iterable

class AliyunBucket(RemoteBucket):
    def __init__(self, bucket_name: str, access_key_id: str, access_key_secret: str, region: str, **kwargs):
        self.bucket_name = bucket_name
        cfg = _oss.config.load_default()
        cfg.credentials_provider = _oss.credentials.StaticCredentialsProvider(access_key_id, access_key_secret)
        cfg.region = region
        if kwargs.get('use_internal_endpoint') is True:
            cfg.use_internal_endpoint = True

        self.client = _oss.Client(cfg)

    def list_files(self, prefix: str) -> Iterable[str]:
        paginator = self.client.list_objects_v2_paginator()
        req = _oss.ListObjectsV2Request(bucket=self.bucket_name, prefix=prefix)
        for page in paginator.iter_page(req):
            for obj in page.contents:
                yield obj.key


    def get_file_content(self, key: str) -> Iterable[bytes]:
        req = _oss.GetObjectRequest(bucket=self.bucket_name, key=key)
        body: _oss.types.StreamBody = self.client.get_object(req).body
        yield from body.iter_bytes()
