import asyncio

from httpclient.domain.float.endpoints import CheckFloatsEndpoint
from httpclient.domain.float.providers import FloatProvider
from httpclient.http_client_factory import create_client

TILLO_HOST = ''
TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}


def check_floats(**kwargs):
    tillo_client = create_client(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILLO_HTTP_CLIENT_OPTIONS,
    )

    query = CheckFloatsEndpoint.QueryParams(**kwargs)
    provider = FloatProvider(tillo_client)
    floats = provider.check_floats(query)

    print(floats.text)


check_floats()

async def check_floats_async(**kwargs):
    tillo_client = create_client(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILLO_HTTP_CLIENT_OPTIONS,
    )

    query = CheckFloatsEndpoint.QueryParams(**kwargs)
    provider = FloatProvider(tillo_client)
    floats = await provider.check_floats(query)

    print(floats.text)


asyncio.run(check_floats_async())