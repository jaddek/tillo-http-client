from dataclasses import dataclass

from ...endpoint import Endpoint, QP
from ...helpers import filter_none_values


class BrandEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'brands'
    _route: str = '/api/v2/brands'

    @dataclass(frozen=True)
    class QueryParams(QP):
        detail: bool = None
        currency: str | None = None
        country: str | None = None
        brand: str | None = None
        category: str | None = None

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)

    @property
    def query(self) -> QueryParams:
        query = self._query

        if query is None:
            query = {}

        return self.QueryParams(**query)


class TemplateListEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'templates'
    _route: str = '/api/v2/templates'

    @dataclass(frozen=True)
    class QueryParams(QP):
        brand: str | None = None

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()

    @property
    def query(self) -> QueryParams:
        query = self._query

        if query is None:
            query = {}

        return self.QueryParams(**query)


class TemplateEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'template'
    _route: str = '/api/v2/template'

    @dataclass(frozen=True)
    class QueryParams(QP):
        brand: str | None = None
        template: str | None = None

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()

    @property
    def query(self) -> QueryParams:
        query = self._query

        if query is None:
            query = {}

        return self.QueryParams(**query)
