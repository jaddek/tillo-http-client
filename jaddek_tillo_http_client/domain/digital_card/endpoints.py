from dataclasses import dataclass, field

from . import FaceValue
from ...endpoint import Endpoint, AbstractBodyRequest, QP
from ...helpers import filter_none_values, transform_to_dict


class IssueDigitalCodeEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'digital-issue'
    _route: str = '/api/v2/digital/issue'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class Personalisation:
            to_name: str | None = None
            from_name: str | None = None
            message: str | None = None
            template: str = 'standard'

        @dataclass(frozen=True)
        class PersonalisationExtended(Personalisation):
            email_message: str | None = None,
            redemption_message: str | None = None,
            carrier_message: str | None = None,

        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: str | None = None
            to_email: str | None = None
            from_name: str | None = None
            from_email: str | None = None
            subject: str | None = None

        @dataclass(frozen=True)
        class FulfilmentParametersForRewardPassUsingEmail:
            to_name: str | None = None
            to_email: str | None = None
            from_name: str | None = None
            from_email: str | None = None
            subject: str | None = None
            language: str = 'en'
            customer_id: str = ""
            to_first_name: str | None = None
            to_last_name: str | None = None

        @dataclass(frozen=True)
        class FulfilmentParametersForRewardPassUsingUrl:
            to_name: str | None = None
            to_first_name: str | None = None
            to_last_name: str | None = None
            address_1: str | None = None
            address_2: str | None = None
            city: str | None = None
            postal_code: str | None = None
            country: str | None = None
            language: str | None = None
            customer_id: str | None = None

        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        delivery_method: str | None = None
        fulfilment_by: str | None = None
        fulfilment_parameters: FulfilmentParameters | FulfilmentParametersForRewardPassUsingEmail | FulfilmentParametersForRewardPassUsingUrl | None = field(
            default=None)
        sector: str | None = None
        personalisation: Personalisation | PersonalisationExtended | None = None

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )


class TopUpDigitalCodeEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'digital-top-up'
    _route: str = '/api/v2/digital/top-up'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None,
        pin: str | None = None,
        sector: str | None = None

        def get_sign_attr(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )

        def get_as_dict(self) -> dict:
            return transform_to_dict(self)


class CheckStockEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'check-stock'
    _route: str = '/api/v2/check-stock'

    @dataclass(frozen=True)
    class QueryParams:
        brand: str = None

        def get_sign_attr(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)


class CancelDigitalCodeEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'digital-issue'
    _route: str = '/api/v2/digital/issue'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        original_client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None,
        sector: str | None = None

        def get_sign_attr(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )

        def get_as_dict(self) -> dict:
            return transform_to_dict(self)


class CancelDigitalUrlEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'digital-issue'
    _route: str = '/api/v2/digital/issue'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        original_client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        url: str | None = None,
        sector: str | None = None

        def get_sign_attr(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )

        def get_as_dict(self) -> dict:
            return transform_to_dict(self)


class ReverseDigitalCode(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'digital-reverse'
    _route: str = '/api/v2/digital/reverse'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        original_client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        sector: str | None = None

        def get_sign_attr(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )

        def get_as_dict(self) -> dict:
            return transform_to_dict(self)


class CheckBalanceEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'digital-check-balance'
    _route: str = '/api/v2/digital/check-balance'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        reference: str | None = None

        def get_sign_attr(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
            )

        def get_as_dict(self) -> dict:
            return transform_to_dict(self)


class OrderDigitalCodeAsyncEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'digital-order-card'
    _route: str = '/api/v2/digital/order-card'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class Personalisation:
            to_name: str | None = None
            from_name: str | None = None
            message: str | None = None
            template: str | None = field(default='standard')
            email_message: str | None = None,
            redemption_message: str | None = None,
            carrier_message: str | None = None,

        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: str | None = None
            to_email: str | None = None
            from_name: str | None = None
            from_email: str | None = None
            subject: str | None = None
            language: str = field(default='en')
            customer_id: str | None = field(default="")
            to_first_name: str | None = None
            to_last_name: str | None = None

        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        delivery_method: str | None = None
        fulfilment_by: str | None = None
        fulfilment_parameters: FulfilmentParameters | None = field(
            default=None)
        sector: str | None = None
        personalisation: Personalisation | None = None

        def get_sign_attr(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )

        def get_as_dict(self) -> dict:
            return transform_to_dict(self)


class CheckDigitalOrderStatusAsyncEndpoint(Endpoint):
    _method: str = 'GET'
    _endpoint: str = 'digital-order-status'
    _route: str = '/api/v2/digital/order-status'

    @dataclass(frozen=True)
    class QueryParams(QP):
        reference: str | None = None

        def get_sign_attr(self) -> tuple:
            return ()

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)
