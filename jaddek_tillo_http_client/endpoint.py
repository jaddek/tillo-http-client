from abc import ABC
from dataclasses import dataclass

from jaddek_tillo_http_client.helpers import filter_none_values


@dataclass(frozen=True)
class QP(ABC):
    def get_not_empty_values(self) -> dict:
        return filter_none_values(self)

    def get_sign_attrs(self) -> tuple | None:
        return None


class Endpoint(ABC):
    _method: str | None = None
    _endpoint: str | None = None
    _route: str | None = None
    _query = None,
    _body = None,
    _sign_attrs = None

    def __init__(
            self,
            query: None | dict = None,
            body: None | dict = None,
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
    def body(self) -> dict:
        return {} if self._body is None else self._body

    @property
    def sign_attrs(self) -> tuple | None:
        return self._sign_attrs

    @property
    def query(self) -> QP:
        return QP()

    @property
    def params(self) -> dict:
        return self.query.get_not_empty_values()
