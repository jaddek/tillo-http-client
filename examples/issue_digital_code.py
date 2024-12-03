import asyncio

from jaddek_tillo_http_client.domain.digital_card.factory import create_standard_issue_request
from jaddek_tillo_http_client.domain.digital_card.services import IssueDigitalCodeService
from jaddek_tillo_http_client.domain.float.services import FloatServices
from jaddek_tillo_http_client.enums import Currency
from jaddek_tillo_http_client.http_client_factory import create_client, create_client_async
import uuid

TILLO_HOST = ''
TILLO_API_KEY = ''
TILLO_SECRET = ''
TILLO_HTTP_CLIENT_OPTIONS = {}


def issue_digital_code():
    sync_client = create_client(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_standard_issue_request(
        client_request_id=str(uuid.uuid4()),
        brand='costa',
        currency=Currency.GBP,
        amount=10,
    )

    response = IssueDigitalCodeService.issue_digital_code(sync_client)

    print(response.text)


issue_digital_code()


async def issue_digital_code_async():
    async_client = create_client_async(
        TILLO_API_KEY,
        TILLO_SECRET,
        TILLO_HTTP_CLIENT_OPTIONS
    )

    body = create_standard_issue_request(
        client_request_id=str(uuid.uuid4()),
        brand='costa',
        currency=Currency.GBP,
        amount=10,
    )

    response = await IssueDigitalCodeService.issue_digital_code_async(
        async_client,
        body=body
    )

    print(response.text)


asyncio.run(issue_digital_code_async())
