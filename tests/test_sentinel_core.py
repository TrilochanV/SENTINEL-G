from sentinel_core import SentinelPipeline
from sentinel_core.schemas import TransactionEvent

def test_pipeline_returns_risk():
    p=SentinelPipeline()
    e=TransactionEvent("t1","a","b",1000,1.0,"d1","10.0.0.1")
    r=p.process(e,0.2)
    assert 0 <= r.risk_score <= 1
    assert r.decision in {"LOW","MEDIUM","HIGH"}
