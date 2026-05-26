import abc
from typing import Iterable, Protocol

class RemoteBucket(abc.ABC):
    @abc.abstractmethod
    def list_files(self, prefix: str) -> Iterable[str]: ...
    
    @abc.abstractmethod
    def get_file_content(self, key: str) -> Iterable[bytes]: ...

class RemoteBucketConstructor(Protocol):
    def __call__(self, bucket_name: str, access_key_id: str, access_key_secret: str, region: str, **kwargs) -> RemoteBucket: ...
