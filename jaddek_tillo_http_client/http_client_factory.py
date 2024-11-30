import httpx

from .http_client import AsyncHttpClient, HttpClient
from .signature import SignatureBridge, SignatureGenerator


def create_signer(
        api_key: str,
        secret_key: str
) -> SignatureBridge:
    return SignatureBridge(
        SignatureGenerator(
            api_key,
            secret_key,
        )
    )


def create_client_async(
        base_url: str,
        api_key: str,
        secret_key: str,
        **kwargs,
) -> AsyncHttpClient:
    signer = create_signer(api_key, secret_key)

    return AsyncHttpClient(
        httpx.AsyncClient(base_url=base_url, **kwargs),
        signer
    )


def create_client(
        base_url: str,
        api_key: str,
        secret_key: str,
        **kwargs,
) -> HttpClient:
    signer = create_signer(api_key, secret_key)

    return HttpClient(
        httpx.Client(base_url=base_url, **kwargs),
        signer
    )
