from . import FaceValue
from .endpoints import ActivatePhysicalCardEndpoint
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
