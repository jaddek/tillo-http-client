from abc import abstractmethod

from httpx import Client, AsyncClient

from .endpoint import Endpoint
from .signature import SignatureBridge


class AbstractClient:
    _signer: SignatureBridge

    def __init__(
            self,
            tillo_client_options: dict,
            signer: SignatureBridge
    ):
        self.tillo_client_options = tillo_client_options
        self._signer = signer

    @abstractmethod
    def request(
            self,
            endpoint: Endpoint,
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
    async def request(
            self,
            endpoint: Endpoint,
    ):
        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            endpoint.query.get_sign_attrs(),
        )

        async with AsyncClient(**self.tillo_client_options) as client:
            response = await client.request(
                url=endpoint.route,
                method=endpoint.method,
                params=endpoint.params,
                json=endpoint.body,
                headers=headers,
            )

        return response


class HttpClient(AbstractClient):
    def request(
            self,
            endpoint: Endpoint,
    ):
        headers = self._get_request_headers(
            endpoint.method,
            endpoint.endpoint,
            endpoint.query.get_sign_attrs(),
        )

        response = Client(**self.tillo_client_options).request(
            url=endpoint.route,
            method=endpoint.method,
            params=endpoint.params,
            json=endpoint.body,
            headers=headers,
        )

        return response
