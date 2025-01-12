from jaddek_tillo_http_client.endpoint import Endpoint


class ActivatePhysicalCardEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-activate'
    _route: str = '/api/v2/physical/activate'


class CancelActivatePhysicalCardEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'activate-physical-card????'
    _route: str = '/api/v2/physical/activate'


class CashOutOriginalTransactionPhysicalCardEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'cash-out-original-transaction'
    _route: str = '/api/v2/physical/cash-out-original-transaction'


class TopUpPhysicalCardEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-top-up'
    _route: str = '/api/v2/physical/top-up'


class CancelTopUpOnPhysicalCardEndpoint(Endpoint):
    _method: str = 'DELETE'
    _endpoint: str = 'physical-top-up'
    _route: str = '/api/v2/physical/top-up'


class OrderPhysicalCard(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-order-card'
    _route: str = '/api/v2/physical/order-card'


class PhysicalCardOrderStatusEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-order-status'
    _route: str = '/api/v2/physical/order-status'


class FulfilPhysicalCardOrderEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-fulfil-order'
    _route: str = '/api/v2/physical/fulfil-order'


class BalanceCheckPhysicalEndpoint(Endpoint):
    _method: str = 'POST'
    _endpoint: str = 'physical-check-balance'
    _route: str = '/api/v2/physical/check-balance'
