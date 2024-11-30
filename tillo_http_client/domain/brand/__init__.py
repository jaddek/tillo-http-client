from dataclasses import field, dataclass


@dataclass(frozen=True)
class FaceValue:
    amount: float | None = field(default=None)
    currency: str | None = field(default=None)
