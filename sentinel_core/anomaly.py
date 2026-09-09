import numpy as np
try:
    from sklearn.ensemble import IsolationForest
except ImportError:
    IsolationForest=None

class AnomalyDetector:
    """Optional unsupervised anomaly layer. Falls back safely until trained."""
    def __init__(self, contamination=0.02):
        self.model=IsolationForest(contamination=contamination, random_state=42) if IsolationForest else None
        self.trained=False
    def fit(self, rows):
        if self.model and len(rows)>=20:
            self.model.fit(np.asarray(rows)); self.trained=True
    def score(self, row):
        if not self.trained: return 0.0
        raw=float(-self.model.decision_function([row])[0])
        return max(0.0,min(1.0,raw+0.5))
