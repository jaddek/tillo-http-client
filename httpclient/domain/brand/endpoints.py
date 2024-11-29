from dataclasses import dataclass, field

from ...endpoint import Endpoint
from ...helpers import filter_none_values


class BrandEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'brands'
    _route: str = '/api/v2/brands'

    @dataclass(frozen=True)
    class QueryParams:
        detail: bool = field(default=True)
        currency: str | None = field(default=None)
        country: str | None = field(default=None)
        brand: str | None = field(default=None)
        category: str | None = field(default=None)

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)


class TemplateListEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'templates'
    _route: str = '/api/v2/templates'

    @dataclass(frozen=True)
    class QueryParams:
        brand: str | None = field(default=None)

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()


class TemplateEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'template'
    _route: str = '/api/v2/template'

    @dataclass(frozen=True)
    class QueryParams:
        brand: str | None = field(default=None)
        template: str | None = field(default=None)

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()
