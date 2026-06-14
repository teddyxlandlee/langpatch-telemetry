import abc
from typing import Iterable, Protocol

class RemoteBucket(abc.ABC):
    @abc.abstractmethod
    def list_files(self, prefix: str) -> Iterable[str]: ...
    
    @abc.abstractmethod
    def get_file_content(self, key: str) -> Iterable[bytes]: ...

    @abc.abstractmethod
    def delete_files(self, keys: list[str]) -> Iterable[str]:
        '''
        @param keys must not exceed 1000 items.
        @return error messages.
        '''
        ...

class RemoteBucketConstructor(Protocol):
    def __call__(self, bucket_name: str, access_key_id: str, access_key_secret: str, region: str, **kwargs) -> RemoteBucket: ...
