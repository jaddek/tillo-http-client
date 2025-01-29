from httpx import Response

from .endpoints import ActivatePhysicalCardEndpoint, CancelActivatePhysicalCardEndpoint, \
    CashOutOriginalTransactionPhysicalCardEndpoint
from ...http_client import HttpClient, AsyncHttpClient


class PhysicalGiftCardsService:
    @staticmethod
    def activate_physical_card(
            client: HttpClient,
            query_params: dict | None = None,
            body: ActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
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
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cancel_activate_physical_card(
            client: HttpClient,
            query_params: dict | None = None,
            body: CancelActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(
            endpoint=endpoint
        )

        return response

    @staticmethod
    async def cancel_activate_physical_card_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: CancelActivatePhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CancelActivatePhysicalCardEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cash_out_original_transaction_physical_card(
            client: HttpClient,
            query_params: dict | None = None,
            body: CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = ActivatePhysicalCardEndpoint(
            body=body,
            query=query_params,
        )

        response = client.request(
            endpoint=endpoint
        )

        return response

    @staticmethod
    async def cash_out_original_transaction_physical_card_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody | None = None,
    ) -> Response:
        endpoint = CashOutOriginalTransactionPhysicalCardEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def top_up_physical_card(self):
        pass

    @staticmethod
    async def top_up_physical_card_async(self):
        pass

    @staticmethod
    def cancel_top_up_on_physical_card(self):
        pass

    @staticmethod
    async def cancel_top_up_on_physical_card_async(self):
        pass

    @staticmethod
    def order_physical_card(self):
        pass

    @staticmethod
    async def order_physical_card_async(self):
        pass

    @staticmethod
    def physical_card_order_status(self):
        pass

    @staticmethod
    async def physical_card_order_status_async(self):
        pass

    @staticmethod
    def fulfil_physical_card_order(self):
        pass

    @staticmethod
    async def fulfil_physical_card_order_async(self):
        pass

    @staticmethod
    def balance_check_physical(self):
        pass

    @staticmethod
    async def balance_check_physical_async(self):
        pass
