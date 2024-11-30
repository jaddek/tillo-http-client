from dataclasses import dataclass, field

from ..brand import FaceValue
from ...endpoint import Endpoint
from ...helpers import filter_none_values, transform_to_dict


class IssueDigitalCodeEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'digital-issue'
    _route: str = '/api/v2/digital/issue'

    @dataclass(frozen=True)
    class RequestBody:
        @dataclass(frozen=True)
        class Personalisation:
            to_name: str | None = field(default=None)
            from_name: str | None = field(default=None)
            message: str | None = field(default=None)
            template: str | None = field(default='standard')

        @dataclass(frozen=True)
        class PersonalisationExtended(Personalisation):
            email_message: str | None = field(default=None),
            redemption_message: str | None = field(default=None),
            carrier_message: str | None = field(default=None),

        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: str | None = field(default=None)
            to_email: str | None = field(default=None)
            from_name: str | None = field(default=None)
            from_email: str | None = field(default=None)
            subject: str | None = field(default=None)

        @dataclass(frozen=True)
        class FulfilmentParametersForRewardPassUsingEmail:
            to_name: str | None = field(default=None)
            to_email: str | None = field(default=None)
            from_name: str | None = field(default=None)
            from_email: str | None = field(default=None)
            subject: str | None = field(default=None)
            language: str = field(default='en')
            customer_id: str | None = field(default="")
            to_first_name: str | None = field(default=None)
            to_last_name: str | None = field(default=None)

        @dataclass(frozen=True)
        class FulfilmentParametersForRewardPassUsingUrl:
            to_name: str | None = field(default=None)
            to_first_name: str | None = field(default=None)
            to_last_name: str | None = field(default=None)
            address_1: str | None = field(default=None)
            address_2: str | None = field(default=None)
            city: str | None = field(default=None)
            postal_code: str | None = field(default=None)
            country: str | None = field(default=None)
            language: str | None = field(default=None)
            customer_id: str | None = field(default=None)

        client_request_id: str | None = field(default=None)
        brand: str | None = field(default=None)
        face_value: FaceValue | None = field(default=None)
        delivery_method: str | None = field(default=None)
        fulfilment_by: str | None = field(default=None)
        fulfilment_parameters: FulfilmentParameters | FulfilmentParametersForRewardPassUsingEmail | FulfilmentParametersForRewardPassUsingUrl | None = field(
            default=None)
        sector: str | None = field(default=None)
        personalisation: Personalisation | PersonalisationExtended | None = field(default=None)

        def get_sign_attr(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )

        def get_as_dict(self) -> dict:
            return transform_to_dict(self)


class TopUpDigitalCodeEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'digital-top-up'
    _route: str = '/api/v2/digital/top-up'

    @dataclass(frozen=True)
    class RequestBody:
        client_request_id: str | None = field(default=None)
        brand: str | None = field(default=None)
        face_value: FaceValue | None = field(default=None)
        code: str | None = field(default=None),
        pin: str | None = field(default=None),
        sector: str | None = field(default=None)

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
        brand: str = field(default=None)

        def get_sign_attr(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)


class CancelDigitalCodeEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'digital-issue'
    _route: str = '/api/v2/digital/issue'

    @dataclass(frozen=True)
    class RequestBody:
        client_request_id: str | None = field(default=None)
        original_client_request_id: str | None = field(default=None)
        brand: str | None = field(default=None)
        face_value: FaceValue | None = field(default=None)
        code: str | None = field(default=None),
        sector: str | None = field(default=None)

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
    class RequestBody:
        client_request_id: str | None = field(default=None)
        original_client_request_id: str | None = field(default=None)
        brand: str | None = field(default=None)
        face_value: FaceValue | None = field(default=None)
        url: str | None = field(default=None),
        sector: str | None = field(default=None)

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
    class RequestBody:
        client_request_id: str | None = field(default=None)
        original_client_request_id: str | None = field(default=None)
        brand: str | None = field(default=None)
        face_value: FaceValue | None = field(default=None)
        sector: str | None = field(default=None)

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
    class RequestBody:
        client_request_id: str | None = field(default=None)
        brand: str | None = field(default=None)
        face_value: FaceValue | None = field(default=None)
        reference: str | None = field(default=None)

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
    class RequestBody:
        @dataclass(frozen=True)
        class Personalisation:
            to_name: str | None = field(default=None)
            from_name: str | None = field(default=None)
            message: str | None = field(default=None)
            template: str | None = field(default='standard')
            email_message: str | None = field(default=None),
            redemption_message: str | None = field(default=None),
            carrier_message: str | None = field(default=None),

        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: str | None = field(default=None)
            to_email: str | None = field(default=None)
            from_name: str | None = field(default=None)
            from_email: str | None = field(default=None)
            subject: str | None = field(default=None)
            language: str = field(default='en')
            customer_id: str | None = field(default="")
            to_first_name: str | None = field(default=None)
            to_last_name: str | None = field(default=None)

        client_request_id: str | None = field(default=None)
        brand: str | None = field(default=None)
        face_value: FaceValue | None = field(default=None)
        delivery_method: str | None = field(default=None)
        fulfilment_by: str | None = field(default=None)
        fulfilment_parameters: FulfilmentParameters | None = field(
            default=None)
        sector: str | None = field(default=None)
        personalisation: Personalisation | None = field(default=None)

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
    class QueryParams:
        reference: str | None = field(default=None)

        def get_sign_attr(self) -> tuple:
            return ()

        def get_not_empty_values(self) -> dict:
            return filter_none_values(self)
