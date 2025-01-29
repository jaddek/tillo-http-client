from . import FaceValue
from .endpoints import ActivatePhysicalCardEndpoint, CashOutOriginalTransactionPhysicalCardEndpoint, \
    TopUpPhysicalCardEndpoint, CancelTopUpOnPhysicalCardEndpoint, BalanceCheckPhysicalEndpoint
from ...enums import Currency, Sector


def create_activate_physical_card_request(
        client_request_id: str,
        brand: str,
        amount: str,
        code: str,
        pin: str,
        currency: Currency.EUR,
        sector: Sector = Sector.GIFT_CARD_MALL,
) -> ActivatePhysicalCardEndpoint.RequestBody:
    return ActivatePhysicalCardEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        code=code,
        pin=pin,
        sector=sector.value,
    )


def create_cash_out_original_transaction_request(
        client_request_id: str,
        original_client_request_id: str,
        brand: str,
        code: str,
        pin: str,
        sector: Sector = Sector.GIFT_CARD_MALL,
) -> CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody:
    return CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody(
        client_request_id=client_request_id,
        original_client_request_id=original_client_request_id,
        brand=brand,
        code=code,
        pin=pin,
        sector=sector.value,
    )


def create_top_up_physical_card_request(
        client_request_id: str,
        brand: str,
        amount: str,
        code: str,
        pin: str,
        currency: Currency.EUR,
        sector: Sector = Sector.GIFT_CARD_MALL,
) -> TopUpPhysicalCardEndpoint.RequestBody:
    return TopUpPhysicalCardEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        code=code,
        pin=pin,
        sector=sector.value,
    )


def create_cancel_top_up_physical_card_request(
        client_request_id: str,
        original_client_request_id: str,
        brand: str,
        amount: str,
        code: str,
        pin: str,
        currency: Currency.EUR,
        sector: Sector = Sector.GIFT_CARD_MALL,
) -> CancelTopUpOnPhysicalCardEndpoint.RequestBody:
    return CancelTopUpOnPhysicalCardEndpoint.RequestBody(
        client_request_id=client_request_id,
        original_client_request_id=original_client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        code=code,
        pin=pin,
        sector=sector.value,
    )


def create_balance_check_request(
        client_request_id: str,
        brand: str,
        code: str,
        pin: str,
        currency: Currency.EUR,
        sector: Sector = Sector.GIFT_CARD_MALL,
) -> BalanceCheckPhysicalEndpoint.RequestBody:
    return BalanceCheckPhysicalEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
        ),
        code=code,
        pin=pin,
        sector=sector.value,
    )
