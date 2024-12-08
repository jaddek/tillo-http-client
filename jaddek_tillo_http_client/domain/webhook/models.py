from dataclasses import dataclass

from .enums import Types


@dataclass(frozen=True)
class Webhook:
    type: str | Types
    timestamp: str
    certificate: str
    version: int
    data: object


@dataclass(frozen=True)
class Status:
    code: str | None = None
    reason: str | None = None


@dataclass(frozen=True)
class Brand:
    name: str | None = None
    slug: str | None = None
    status: Status = Status


@dataclass(frozen=True)
class BrandList:
    brands: list[Brand] = list
