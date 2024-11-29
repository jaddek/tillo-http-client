from abc import ABC

class Endpoint(ABC):
    _method: str | None = None
    _endpoint: str | None = None
    _route: str | None = None

    @property
    def method(self):
        return self._method

    @property
    def endpoint(self):
        return self._endpoint

    @property
    def route(self):
        return self._route