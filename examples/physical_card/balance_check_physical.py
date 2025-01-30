import asyncio
import uuid

from jaddek_tillo_http_client.domain.physical_card.factory import create_activate_physical_card_request, \
    create_balance_check_request
from jaddek_tillo_http_client.domain.physical_card.services import PhysicalGiftCardsService
from jaddek_tillo_http_client.enums import Currency
from jaddek_tillo_http_client.http_client_factory import create_client, create_client_async

TILLO_HOST = ''
TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}


def balance_check_physical():
    sync_client = create_client(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_balance_check_request(
        client_request_id=str(uuid.uuid4()),
        brand='costa',
        currency=Currency.GBP,
        code="ABCD12324",
        pin="",
    )

    return PhysicalGiftCardsService.balance_check_physical(
        client=sync_client,
        body=body
    )


print(balance_check_physical().json())


async def balance_check_physical_async():
    async_client = create_client_async(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_balance_check_request(
        client_request_id=str(uuid.uuid4()),
        brand='costa',
        currency=Currency.GBP,
        code="ABCD12324",
        pin="",
    )

    return await PhysicalGiftCardsService.balance_check_physical_async(
        client=async_client,
        body=body
    )


asyncio.run(balance_check_physical_async())
