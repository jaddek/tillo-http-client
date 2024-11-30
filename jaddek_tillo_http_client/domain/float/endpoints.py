from dataclasses import dataclass, field

from ...endpoint import Endpoint
from ...helpers import filter_none_values


class CheckFloatsEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'check-floats'
    _route: str = '/api/v2/check-floats'

    @dataclass(frozen=True)
    class QueryParams:
        currency: str = field(default=None)
        template: str = field(default=None)

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)
