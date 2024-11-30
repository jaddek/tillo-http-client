from abc import ABC

from .http_client import AbstractClient


class Provider(ABC):
    def __init__(
            self,
            http_client: AbstractClient,
    ):
        self.__http_client = http_client

    @property
    def http_client(self) -> AbstractClient:
        return self.__http_client
