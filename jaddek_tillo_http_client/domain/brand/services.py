from jaddek_tillo_http_client.domain.brand.endpoints import BrandEndpoint, TemplateListEndpoint, TemplateEndpoint
from jaddek_tillo_http_client.http_client import HttpClient, AsyncHttpClient


class BrandAssetsService:
    @staticmethod
    def get_available_brands(
            client: HttpClient,
            query_params: dict | None = None,
    ) -> any:
        endpoint = BrandEndpoint(query=query_params)

        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def get_available_brands_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
    ):
        endpoint = BrandEndpoint(query=query_params)
        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    async def get_brand_templates_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
    ):
        endpoint = TemplateListEndpoint(query_params)
        response = await client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def get_brand_templates(
            client: HttpClient,
            query_params: dict | None = None,
    ):
        endpoint = TemplateListEndpoint(query_params)
        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def download_brand_template(
            client: HttpClient,
            query_params: dict | None = None,
    ):
        endpoint = TemplateEndpoint(query_params)
        response = client.request(
            endpoint=endpoint,
        )

        return response

    @staticmethod
    def download_brand_template_async(
            client: AsyncHttpClient,
            query_params: dict | None = None,
    ):
        endpoint = TemplateEndpoint(query_params)
        response = client.request(
            endpoint=endpoint,
        )

        return response
