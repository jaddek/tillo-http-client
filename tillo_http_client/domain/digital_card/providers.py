from .endpoints import IssueDigitalCodeEndpoint, \
    TopUpDigitalCodeEndpoint, CheckStockEndpoint, CheckBalanceEndpoint, CancelDigitalCodeEndpoint, \
    CancelDigitalUrlEndpoint, ReverseDigitalCode, OrderDigitalCodeAsyncEndpoint, CheckDigitalOrderStatusAsyncEndpoint
from ...provider import Provider


class IssueDigitalCode(Provider):
    def issue_digital_code(
            self,
            body: IssueDigitalCodeEndpoint.RequestBody
    ):
        response = self.http_client.request(
            IssueDigitalCodeEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
            params={}
        )

        return response

    async def issue_digital_code_async(
            self,
            body: IssueDigitalCodeEndpoint.RequestBody
    ):
        response = await self.http_client.request(
            IssueDigitalCodeEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response


class IssueDigitalCodeAsync(Provider):
    def order_digital_code(
            self,
            body: OrderDigitalCodeAsyncEndpoint.RequestBody
    ):
        response = self.http_client.request(
            OrderDigitalCodeAsyncEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    async def order_digital_code_async(
            self,
            body: OrderDigitalCodeAsyncEndpoint.RequestBody
    ):
        response = await self.http_client.request(
            OrderDigitalCodeAsyncEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    def check_digital_order_status(
            self,
            query: CheckDigitalOrderStatusAsyncEndpoint.QueryParams
    ):
        response = self.http_client.request(
            OrderDigitalCodeAsyncEndpoint(),
            sign_attrs=query.get_sign_attr(),
            params=query.get_not_empty_values()
        )

        return response

    async def check_digital_order_status_async(
            self,
            query: CheckDigitalOrderStatusAsyncEndpoint.QueryParams
    ):
        response = await self.http_client.request(
            OrderDigitalCodeAsyncEndpoint(),
            sign_attrs=query.get_sign_attr(),
            params=query.get_not_empty_values()
        )

        return response


class TopUpDigitalCode(Provider):
    async def top_up_digital_code_async(
            self,
            body: TopUpDigitalCodeEndpoint.RequestBody
    ):
        response = await self.http_client.request(
            TopUpDigitalCodeEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    def top_up_digital_code(
            self,
            body: TopUpDigitalCodeEndpoint.RequestBody
    ):
        response = self.http_client.request(
            TopUpDigitalCodeEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response


class CancelDigitalCode(Provider):
    def cancel_digital_code(
            self,
            body: CancelDigitalCodeEndpoint.RequestBody
    ):
        response = self.http_client.request(
            CancelDigitalUrlEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    async def cancel_digital_code_async(
            self,
            body: CancelDigitalCodeEndpoint.RequestBody
    ):
        response = await self.http_client.request(
            CancelDigitalCodeEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    def cancel_digital_url(
            self,
            body: CancelDigitalUrlEndpoint.RequestBody
    ):
        response = self.http_client.request(
            CancelDigitalCodeEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    async def cancel_digital_url_async(
            self,
            body: CancelDigitalUrlEndpoint.RequestBody
    ):
        response = await self.http_client.request(
            CancelDigitalCodeEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    def reverse_digital_code(
            self,
            body: ReverseDigitalCode.RequestBody
    ):
        response = self.http_client.request(
            ReverseDigitalCode(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    async def reverse_digital_code_async(
            self,
            body: ReverseDigitalCode.RequestBody
    ):
        response = await self.http_client.request(
            ReverseDigitalCode(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response


class StockProvider(Provider):
    def check_stock(
            self,
            query: CheckStockEndpoint.QueryParams
    ):
        response = self.http_client.request(
            CheckStockEndpoint(),
            params=query.get_not_empty_values(),
            sign_attrs=query.get_sign_attr(),
        )

        return response

    async def check_stock_async(
            self,
            query: CheckStockEndpoint.QueryParams
    ):
        response = await self.http_client.request(
            CheckStockEndpoint(),
            params=query.get_not_empty_values(),
            sign_attrs=query.get_sign_attr(),
        )

        return response


class BalanceProvider(Provider):
    def check_balance(
            self,
            body: CheckBalanceEndpoint.RequestBody

    ):
        response = self.http_client.request(
            CheckBalanceEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response

    async def check_balance_async(
            self,
            body: CheckBalanceEndpoint.RequestBody
    ):
        response = await self.http_client.request(
            CheckBalanceEndpoint(),
            body=body.get_as_dict(),
            sign_attrs=body.get_sign_attr(),
        )

        return response
