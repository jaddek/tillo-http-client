import asyncio

from jaddek_tillo_http_client.domain.brand.services import BrandAssetsService
from jaddek_tillo_http_client.http_client import AsyncHttpClient, HttpClient
from jaddek_tillo_http_client.http_client_factory import create_client_async, create_client

TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}


def get_brand_template():
    sync_client: HttpClient = create_client(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    response = BrandAssetsService.get_brand_templates(sync_client)

    print(response.text)


get_brand_template()


async def get_brand_template_async():
    async_client: AsyncHttpClient = create_client_async(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    response = await BrandAssetsService.get_brand_templates_async(async_client)

    print(response.text)


asyncio.run(get_brand_template_async())
