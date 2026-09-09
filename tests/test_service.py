from services.transaction_service import TransactionDetectionService
from repositories.memory import InMemoryStateRepository

def test_service_processes_transaction():
    repo=InMemoryStateRepository(); service=TransactionDetectionService(repository=repo)
    out=service.process({"id":"1","sender":"A","receiver":"B","amount":100,"timestamp":1,"device_id":"D"})
    assert "sentinel_risk_score" in out
    assert len(repo.snapshot()["transactions"])==1
