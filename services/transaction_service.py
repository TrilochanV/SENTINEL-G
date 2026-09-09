import time
from sentinel_core import SentinelPipeline
from sentinel_core.schemas import TransactionEvent

class TransactionDetectionService:
    def __init__(self, pipeline=None, repository=None):
        self.pipeline=pipeline or SentinelPipeline(); self.repository=repository
    def process(self, tx, legacy_aml_score=0.0):
        event=TransactionEvent(
            transaction_id=str(tx.get("transaction_id") or tx.get("id") or f"tx-{time.time_ns()}"),
            sender=str(tx.get("sender") or tx.get("from_account") or tx.get("source") or "unknown"),
            receiver=str(tx.get("receiver") or tx.get("to_account") or tx.get("destination") or "unknown"),
            amount=float(tx.get("amount",0)), timestamp=float(tx.get("timestamp",time.time())),
            device_id=tx.get("device_id"), ip_address=tx.get("ip_address"), fingerprint=tx.get("fingerprint"), metadata=tx,
        )
        result=self.pipeline.process(event,legacy_aml_score)
        output={**tx,"sentinel_risk_score":result.risk_score,"sentinel_decision":result.decision,"sentinel_signals":result.signals,"sentinel_reasons":result.reasons}
        if self.repository:
            self.repository.add_transaction(output)
            if result.decision in {"HIGH","MEDIUM"}: self.repository.add_alert(output)
        return output
