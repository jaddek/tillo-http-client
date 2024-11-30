import asyncio

from jaddek_tillo_http_client.domain.brand.providers import TemplateListProvider
from jaddek_tillo_http_client.http_client_factory import create_client_async, create_client

TILLO_HOST = ''
TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}

def get_brand_templates():
    tillo_client = create_client(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILLO_HTTP_CLIENT_OPTIONS,
    )

    query = TemplateListProvider.get_template_list_endpoint_query()
    provider = TemplateListProvider(tillo_client)
    templates = provider.get_templates(query)

    return templates


get_brand_templates()


async def get_brand_templates_async():
    tillo_async_client = create_client_async(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILLO_HTTP_CLIENT_OPTIONS,
    )

    query = TemplateListProvider.get_template_list_endpoint_query()
    provider = TemplateListProvider(tillo_async_client)
    templates = await provider.get_templates_async(query)

    return templates



asyncio.run(get_brand_templates_async())
