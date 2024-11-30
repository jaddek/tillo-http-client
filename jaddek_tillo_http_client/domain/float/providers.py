from .endpoints import CheckFloatsEndpoint
from ...helpers import filter_none_values
from ...provider import Provider


class FloatProvider(Provider):

    def check_floats(
            self,
            params: CheckFloatsEndpoint.QueryParams
    ):
        response = self.http_client.request(
            CheckFloatsEndpoint(),
            filter_none_values(params),
        )

        return response

    async def check_floats_async(
            self,
            params: CheckFloatsEndpoint.QueryParams,
    ):
        response = await self.http_client.request(
            CheckFloatsEndpoint(),
            filter_none_values(params),
        )

        return response

    def request_payment_transfer(self):
        pass

    async def request_payment_transfer_async(self):
        pass
