from collections import defaultdict, deque
import math

class BehavioralProfiler:
    """Online per-account behavioural baseline with bounded memory."""
    def __init__(self, window=200):
        self.history = defaultdict(lambda: deque(maxlen=window))

    def update(self, account_id, amount, timestamp, counterparty=None):
        self.history[account_id].append((float(amount), float(timestamp), counterparty))

    def features(self, account_id):
        h=list(self.history[account_id])
        if not h: return {"tx_count":0,"velocity_1h":0.0,"amount_zscore":0.0,"amount_entropy":0.0,"unique_counterparties":0}
        amounts=[x[0] for x in h]; now=h[-1][1]
        recent=[x for x in h if now-x[1] <= 3600]
        mean=sum(amounts)/len(amounts)
        variance=sum((a-mean)**2 for a in amounts)/max(1,len(amounts))
        std=math.sqrt(variance)
        z=0.0 if std==0 else abs(amounts[-1]-mean)/std
        buckets=defaultdict(int)
        for a in amounts: buckets[int(math.log10(max(a,1)))] += 1
        entropy=-sum((c/len(amounts))*math.log(c/len(amounts)) for c in buckets.values())
        return {"tx_count":len(h),"velocity_1h":len(recent),"amount_zscore":z,"amount_entropy":entropy,"unique_counterparties":len({x[2] for x in h if x[2]})}
