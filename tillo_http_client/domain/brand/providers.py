from httpx import Response

from .endpoints import BrandEndpoint, TemplateListEndpoint, \
    TemplateEndpoint
from ...provider import Provider


class BrandProvider(Provider):

    @staticmethod
    def get_brand_endpoint_query(**kwargs):
        return BrandEndpoint.QueryParams(**kwargs)

    async def get_brands_async(
            self,
            params: BrandEndpoint.QueryParams
    ) -> Response:
        response = await self.http_client.request(
            BrandEndpoint(),
            params=params.get_not_empty_values()
        )

        return response

    def get_brands(
            self,
            params: BrandEndpoint.QueryParams
    ) -> Response:
        response = self.http_client.request(
            BrandEndpoint(),
            params=params.get_not_empty_values()
        )

        return response


class TemplateListProvider(Provider):
    @staticmethod
    def get_template_list_endpoint_query(**kwargs):
        return TemplateListEndpoint.QueryParams(**kwargs)

    def get_templates(
            self,
            params: TemplateListEndpoint.QueryParams
    ):
        response = self.http_client.request(
            TemplateListEndpoint(),
            params=params.get_not_empty_values()
        )

        return response

    async def get_templates_async(
            self,
            params: TemplateListEndpoint.QueryParams
    ):
        response = await self.http_client.request(
            TemplateListEndpoint(),
            params=params.get_not_empty_values(),
            sign_attrs=params.get_sign_attrs()
        )

        return response


class TemplateProvider(Provider):
    def get_template(
            self,
            params: TemplateEndpoint.QueryParams
    ):
        response = self.http_client.request(
            TemplateEndpoint(),
            params=params.get_not_empty_values(),
            sign_attrs=params.get_sign_attrs()
        )

        return response

    async def get_template_async(
            self,
            params: TemplateEndpoint.QueryParams
    ):
        response = await self.http_client.request(
            TemplateEndpoint(),
            params=params.get_not_empty_values(),
            sign_attrs=params.get_sign_attrs()
        )

        return response
