from abc import ABC, abstractmethod
from dataclasses import dataclass

from .helpers import filter_none_values, transform_to_dict


@dataclass(frozen=True)
class QP(ABC):
    def get_not_empty_values(self) -> dict:
        return filter_none_values(self)

    def get_sign_attrs(self) -> tuple | None:
        return None


@dataclass(frozen=True)
class AbstractBodyRequest(ABC):
    @abstractmethod
    def get_sign_attrs(self) -> tuple:
        pass

    def get_as_dict(self) -> dict:
        return transform_to_dict(self)


class Endpoint(ABC):
    _method: str | None = None
    _endpoint: str | None = None
    _route: str | None = None
    _query = None,
    _body: AbstractBodyRequest | None = None,
    _sign_attrs = None

    def __init__(
            self,
            query: dict | None = None,
            body: AbstractBodyRequest | None = None,
            sign_attrs: tuple | None = None,
    ):
        self._query = query
        self._body = body
        self._sign_attrs = sign_attrs

    @property
    def method(self) -> None | str:
        return self._method

    @property
    def endpoint(self) -> None | str:
        return self._endpoint

    @property
    def route(self) -> None | str:
        return self._route

    @property
    def body(self) -> AbstractBodyRequest | None:
        return {} if self._body is None else self._body

    def is_body_not_empty(self) -> bool:
        return self._body is not None

    @property
    def sign_attrs(self) -> tuple | None:
        return self._sign_attrs

    @property
    def query(self) -> QP:
        return QP()

    @property
    def params(self) -> dict:
        return self.query.get_not_empty_values()
