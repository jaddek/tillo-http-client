import asyncio

from httpclient.domain.brand.providers import BrandProvider
from httpclient.http_client_factory import create_async_client, create_client

TILLO_HOST = ''
TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}


def get_available_brands():
    """
    Get Available Brands using sync client
    :return:
    """
    tillo_client = create_client(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILLO_HTTP_CLIENT_OPTIONS,
    )

    query = BrandProvider.get_brand_endpoint_query()
    provider = BrandProvider(tillo_client)
    brands = provider.get_brands(query)

    print(brands.text)


get_available_brands()


async def get_available_brands_async():
    """
    Get Available Brands using async client
    :return:
    """
    tillo_async_client = create_async_client(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILLO_HTTP_CLIENT_OPTIONS,
    )

    query = BrandProvider.get_brand_endpoint_query()
    provider = BrandProvider(tillo_async_client)
    brands = await provider.get_brands_async(query)

    print(brands.text)


asyncio.run(get_available_brands_async())
