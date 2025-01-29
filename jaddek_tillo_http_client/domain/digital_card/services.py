from .endpoints import IssueDigitalCodeEndpoint, \
    OrderDigitalCodeAsyncEndpoint, CheckDigitalOrderStatusAsyncEndpoint, TopUpDigitalCodeEndpoint, \
    CancelDigitalUrlEndpoint, CancelDigitalCodeEndpoint, ReverseDigitalCode, CheckStockEndpoint, CheckBalanceEndpoint
from ...http_client import HttpClient, AsyncHttpClient


class IssueDigitalCodeService:
    @staticmethod
    def issue_digital_code(
            client: HttpClient,
            query_params: dict | None = None,
            body: IssueDigitalCodeEndpoint.RequestBody | None = None,
    ):
        endpoint = IssueDigitalCodeEndpoint(
            body=body,
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def issue_digital_code_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: IssueDigitalCodeEndpoint.RequestBody | None = None,
    ):
        endpoint = IssueDigitalCodeEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def order_digital_code(
            client: HttpClient,
            query_params: dict | None = None,
            body: OrderDigitalCodeAsyncEndpoint.RequestBody | None = None,
    ):
        endpoint = OrderDigitalCodeAsyncEndpoint(
            body=body,
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def order_digital_code_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: OrderDigitalCodeAsyncEndpoint.RequestBody | None = None,
    ):
        endpoint = OrderDigitalCodeAsyncEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def check_digital_order(
            client: HttpClient,
            query_params: dict | None = None,
    ):
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def check_digital_order_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
    ):
        endpoint = CheckDigitalOrderStatusAsyncEndpoint(
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def top_up_digital_code(
            client: HttpClient,
            query_params: dict | None = None,
            body: TopUpDigitalCodeEndpoint.RequestBody | None = None,
    ):
        endpoint = TopUpDigitalCodeEndpoint(
            body=body,
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def top_up_digital_code_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: TopUpDigitalCodeEndpoint.RequestBody | None = None,
    ):
        endpoint = TopUpDigitalCodeEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cancel_digital_url(
            client: HttpClient,
            query_params: dict | None = None,
            body: CancelDigitalUrlEndpoint.RequestBody | None = None,
    ):
        endpoint = CancelDigitalUrlEndpoint(
            body=body,
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def cancel_digital_url_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: CancelDigitalUrlEndpoint.RequestBody | None = None,
    ):
        endpoint = CancelDigitalUrlEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def cancel_digital_code(
            client: HttpClient,
            query_params: dict | None = None,
            body: CancelDigitalCodeEndpoint.RequestBody | None = None,
    ):
        endpoint = CancelDigitalCodeEndpoint(
            body=body,
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def cancel_digital_code_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: CancelDigitalCodeEndpoint.RequestBody | None = None,
    ):
        endpoint = CancelDigitalCodeEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def reverse_digital_code(
            client: HttpClient,
            query_params: dict | None = None,
            body: ReverseDigitalCode.RequestBody | None = None,
    ):
        endpoint = ReverseDigitalCode(
            body=body,
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def reverse_digital_code_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: ReverseDigitalCode.RequestBody | None = None,
    ):
        endpoint = ReverseDigitalCode(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def check_stock(
            client: AsyncHttpClient,
            query_params: dict | None = None,
    ):
        endpoint = CheckStockEndpoint(
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def check_stock_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
    ):
        endpoint = CheckStockEndpoint(
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def check_balance(
            client: HttpClient,
            query_params: dict | None = None,
            body: CheckBalanceEndpoint.RequestBody | None = None,
    ):
        endpoint = CheckBalanceEndpoint(
            body=body,
            query=query_params
        )

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def check_balance_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
            body: CheckBalanceEndpoint.RequestBody | None = None,
    ):
        endpoint = CheckBalanceEndpoint(
            body=body,
            query=query_params
        )

        response = await client.request(
            endpoint=endpoint,
        )

        return response
