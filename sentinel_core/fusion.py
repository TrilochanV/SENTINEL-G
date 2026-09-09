class RiskFusion:
    DEFAULT_WEIGHTS={"behavior":0.20,"device":0.20,"anomaly":0.15,"graph":0.25,"aml":0.20}
    def __init__(self, weights=None):
        self.weights=weights or self.DEFAULT_WEIGHTS
    def combine(self, signals):
        total=sum(self.weights.get(k,0)*max(0,min(1,float(v))) for k,v in signals.items())
        return round(min(1.0,total),4)
