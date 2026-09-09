from .behavior import BehavioralProfiler
from .device_intelligence import DeviceIntelligence
from .graph_intelligence import GraphIntelligence
from .anomaly import AnomalyDetector
from .fusion import RiskFusion
from .schemas import DetectionResult

class SentinelPipeline:
    """Composable online detection pipeline; AML score may be supplied by legacy engines."""
    def __init__(self):
        self.behavior=BehavioralProfiler(); self.device=DeviceIntelligence(); self.graph=GraphIntelligence(); self.anomaly=AnomalyDetector(); self.fusion=RiskFusion()
    def process(self, event, legacy_aml_score=0.0):
        self.behavior.update(event.sender,event.amount,event.timestamp,event.receiver)
        self.behavior.update(event.receiver,event.amount,event.timestamp,event.sender)
        self.device.observe(event.sender,event.device_id,event.ip_address,event.fingerprint)
        self.graph.observe(event.sender,event.receiver,event.amount)
        b=self.behavior.features(event.sender)
        d=self.device.score(event.sender,event.device_id,event.ip_address,event.fingerprint)
        g=self.graph.features(event.sender)
        behavior_score=min(1.0,b["amount_zscore"]/5 + b["velocity_1h"]/50)
        graph_score=min(1.0,g["degree_ratio"]*2 + g["pagerank"]*10)
        anomaly_row=[event.amount,b["velocity_1h"],b["unique_counterparties"],g["degree_ratio"]]
        a=self.anomaly.score(anomaly_row)
        signals={"behavior":behavior_score,"device":d,"anomaly":a,"graph":graph_score,"aml":legacy_aml_score}
        score=self.fusion.combine(signals)
        reasons=[k for k,v in signals.items() if v>=0.4]
        decision="HIGH" if score>=0.75 else "MEDIUM" if score>=0.45 else "LOW"
        return DetectionResult(event.sender,score,decision,signals,reasons)
