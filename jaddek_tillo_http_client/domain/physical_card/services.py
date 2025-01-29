from jaddek_tillo_http_client.domain.physical_card.endpoints import ActivatePhysicalCardEndpoint
from jaddek_tillo_http_client.http_client import HttpClient, AsyncHttpClient


class PhysicalGiftCardsService:
    @staticmethod
    def activate_physical_card(
            client: HttpClient,
            query_params: dict | None = None,
            body: ActivatePhysicalCardEndpoint.RequestBody | None = None,
    ):
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(
            endpoint=endpoint
        )

        return response

    @staticmethod
    async def activate_physical_card_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: ActivatePhysicalCardEndpoint.RequestBody | None = None,
    ):
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    def cancel_activate_physical_card(self):
        pass

    async def cancel_activate_physical_card_async(self):
        pass

    def cash_out_original_transaction_physical_card(self):
        pass

    async def cash_out_original_transaction_physical_card_async(self):
        pass

    def top_up_physical_card(self):
        pass

    async def top_up_physical_card_async(self):
        pass

    def cancel_top_up_on_physical_card(self):
        pass

    async def cancel_top_up_on_physical_card_async(self):
        pass

    def order_physical_card(self):
        pass

    async def order_physical_card_async(self):
        pass

    def physical_card_order_status(self):
        pass

    async def physical_card_order_status_async(self):
        pass

    def fulfil_physical_card_order(self):
        pass

    async def fulfil_physical_card_order_async(self):
        pass

    def balance_check_physical(self):
        pass

    async def balance_check_physical_async(self):
        pass
