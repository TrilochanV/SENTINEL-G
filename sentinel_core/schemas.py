from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass
class TransactionEvent:
    transaction_id: str
    sender: str
    receiver: str
    amount: float
    timestamp: float
    device_id: Optional[str] = None
    ip_address: Optional[str] = None
    fingerprint: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class DetectionResult:
    account_id: str
    risk_score: float
    decision: str
    signals: Dict[str, float]
    reasons: list[str]
