from abc import abstractmethod

from httpx import Client, AsyncClient

from .endpoint import Endpoint
from .signature import SignatureBridge


class AbstractClient:
    _http_client: Client | AsyncClient
    _signer: SignatureBridge

    def __init__(
            self,
            client: Client | AsyncClient,
            signer: SignatureBridge
    ):
        self.check_client(client)

        self._http_client = client
        self._signer = signer

    @abstractmethod
    def check_client(self, client: Client | AsyncClient):
        pass

    @abstractmethod
    def request(
            self,
            endpoint: Endpoint,
            params: dict | None = None,
            body: dict | None = None,
            sign_attrs: tuple | None = None,
    ):
        pass

    def _get_request_headers(
            self,
            method: str,
            endpoint: str,
            sign_attrs: tuple | None = None,

    ) -> dict:
        (
            request_api_key,
            request_signature,
            request_timestamp
        ) = self._signer.sign(
            endpoint,
            method,
            sign_attrs,
        )

        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'API-Key': request_api_key,
            'Signature': request_signature,
            'Timestamp': request_timestamp,
        }


class AsyncHttpClient(AbstractClient):
    def check_client(self, client: AsyncClient):
        if not isinstance(client, AsyncClient):
            raise TypeError(f'Class should be instance of httpx.AsyncClient')

    async def request(
            self,
            endpoint: Endpoint,
            params: dict | None = None,
            body: dict | None = None,
            sign_attrs: tuple | None = None,
    ):
        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs
        )

        if body is None:
            body = {}

        async with self._http_client as client:
            response = await client.request(
                endpoint.method,
                endpoint.route,
                params=params,
                headers=headers,
                json=body,
            )

            return response


class HttpClient(AbstractClient):
    def check_client(self, client: Client):
        if not isinstance(client, Client):
            raise TypeError(f'Class should be instance of httpx.AsyncClient')

    def request(
            self,
            endpoint: Endpoint,
            params: dict | None = None,
            body: dict | None = None,
            sign_attrs: tuple | None = None,
    ):
        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            sign_attrs
        )

        return self._http_client.request(
            endpoint.method,
            endpoint.route,
            params=params,
            headers=headers,
            json=body,
        )
