from dataclasses import dataclass

from ...endpoint import Endpoint, QP
from ...helpers import filter_none_values


class CheckFloatsEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'check-floats'
    _route: str = '/api/v2/check-floats'

    @dataclass(frozen=True)
    class QueryParams(QP):
        currency: str | None = None
        template: str | None = None

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)
