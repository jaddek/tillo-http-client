import asyncio

from jaddek_tillo_http_client.domain.brand.services import BrandAssetsService
from jaddek_tillo_http_client.http_client_factory import create_client_async, create_client

TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}


def get_available_brands():
    sync_client = create_client(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    response = BrandAssetsService.get_available_brands(sync_client)

    print(response.text)


get_available_brands()


async def get_available_brands_async():
    async_client = create_client_async(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    response = await BrandAssetsService.get_available_brands_async(async_client)

    print(response.text)


asyncio.run(get_available_brands_async())
