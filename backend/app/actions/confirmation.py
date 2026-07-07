from enum import Enum


class RiskLevel(str, Enum):
    SAFE = "safe"
    MEDIUM = "medium"
    HIGH = "high"


def requires_confirmation(risk: RiskLevel) -> bool:
    return risk in (
        RiskLevel.MEDIUM,
        RiskLevel.HIGH,
    )
