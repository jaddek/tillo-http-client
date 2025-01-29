from dataclasses import dataclass

from jaddek_tillo_http_client.domain.physical_card import FaceValue
from jaddek_tillo_http_client.endpoint import Endpoint, AbstractBodyRequest
from jaddek_tillo_http_client.enums import Sector


class ActivatePhysicalCardEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-activate'
    _route: str = '/api/v2/physical/activate'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None,
        brand: str | None = None,
        face_value: FaceValue | None = None,
        code: str | None = None,
        pin: str | None = None,
        sector: Sector | None = Sector.GIFT_CARD_MALL

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )

class CancelActivatePhysicalCardEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'activate-physical-card????'
    _route: str = '/api/v2/physical/activate'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None,
        original_client_request_id: str | None = None,
        brand: str | None = None,
        face_value: FaceValue | None = None,
        code: str | None = None,
        pin: str | None = None,
        sector: Sector | None = Sector.GIFT_CARD_MALL
        tags: list[str] | None = None


class CashOutOriginalTransactionPhysicalCardEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'cash-out-original-transaction'
    _route: str = '/api/v2/physical/cash-out-original-transaction'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None,
        original_client_request_id: str | None = None,
        brand: str | None = None,
        code: str | None = None,
        pin: str | None = None,
        sector: Sector | None = Sector.GIFT_CARD_MALL


class TopUpPhysicalCardEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-top-up'
    _route: str = '/api/v2/physical/top-up'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None,
        brand: str | None = None,
        face_value: FaceValue | None = None,
        code: str | None = None,
        pin: str | None = None,
        sector: Sector | None = Sector.GIFT_CARD_MALL


class CancelTopUpOnPhysicalCardEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'physical-top-up'
    _route: str = '/api/v2/physical/top-up'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None,
        original_client_request_id: str | None = None,
        brand: str | None = None,
        face_value: FaceValue | None = None,
        code: str | None = None,
        pin: str | None = None,
        sector: Sector | None = Sector.GIFT_CARD_MALL


class OrderPhysicalCard(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-order-card'
    _route: str = '/api/v2/physical/order-card'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: str | None = None
            company_name: str | None = None
            address_1: str | None = None
            address_2: str = ""
            address_3: str = ""
            address_4: str = ""
            city: str | None = None
            postal_code: str | None = None
            country: str | None = None

        client_request_id: str | None = None,
        brand: str | None = None,
        face_value: FaceValue | None = None,
        shipping_method: str | None = None,
        fulfilment_by: str | None = None,
        fulfilment_parameters: FulfilmentParameters | None = None,
        personalisation: dict | None = None,
        sector: Sector | None = Sector.GIFT_CARD_MALL,
        tags: list[str] | None = None,


class PhysicalCardOrderStatusEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-order-status'
    _route: str = '/api/v2/physical/order-status'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        references: list[str] | None = None


class FulfilPhysicalCardOrderEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-fulfil-order'
    _route: str = '/api/v2/physical/fulfil-order'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None,
        brand: str | None = None,
        face_value: FaceValue | None = None,
        code: str | None = None,
        references: str | None = None


class BalanceCheckPhysicalEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-check-balance'
    _route: str = '/api/v2/physical/check-balance'

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None,
        brand: str | None = None,
        face_value: FaceValue | None = None,
        code: str | None = None,
        pin: str | None = None,
        sector: Sector | None = Sector.GIFT_CARD_MALL
