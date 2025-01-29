import asyncio
import uuid

from jaddek_tillo_http_client.domain.float.services import FloatService
from jaddek_tillo_http_client.domain.physical_card.factory import create_activate_physical_card_request
from jaddek_tillo_http_client.domain.physical_card.services import PhysicalGiftCardsService
from jaddek_tillo_http_client.enums import Currency
from jaddek_tillo_http_client.http_client_factory import create_client, create_client_async

TILLO_HOST = ''
TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}

def activate_physical_card():
    sync_client = create_client(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_activate_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        brand='costa',
        currency=Currency.GBP,
        amount="10",
        code="ABCD12324",
        pin="",
    )

    return PhysicalGiftCardsService.activate_physical_card(
        client=sync_client,
        body=body
    )

print(activate_physical_card().json())

async def activate_physical_card_async():
    async_client = create_client_async(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_activate_physical_card_request(
        client_request_id=str(uuid.uuid4()),
        brand='costa',
        currency=Currency.GBP,
        amount="10",
        code="ABCD12324",
        pin="",
    )

    return await PhysicalGiftCardsService.activate_physical_card_async(
        client=async_client,
        body=body
    )


asyncio.run(activate_physical_card_async())
