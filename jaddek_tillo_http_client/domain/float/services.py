from .endpoints import CheckFloatsEndpoint
from ...http_client import HttpClient, AsyncHttpClient


class FloatService:
    @staticmethod
    def check_floats(
            client: HttpClient,
            query_params: dict | None = None,
    ):
        endpoint = CheckFloatsEndpoint(
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def check_floats_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
    ):
        endpoint = CheckFloatsEndpoint(
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def request_payment_transfer(self):
        pass

    @staticmethod
    async def request_payment_transfer_async(self):
        pass
