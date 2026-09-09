from collections import deque
from .interfaces import StateRepository

class InMemoryStateRepository(StateRepository):
    """Demo adapter. Replace with PostgreSQL/Redis implementations in production."""
    def __init__(self, account_limit=10000, alert_limit=1000, tx_limit=10000):
        self.accounts={}; self.alerts=deque(maxlen=alert_limit); self.transactions=deque(maxlen=tx_limit)
    def add_account(self, account):
        key=account.get("account_id") or account.get("id") or str(len(self.accounts)); self.accounts[key]=account
    def add_transaction(self, transaction): self.transactions.append(transaction)
    def add_alert(self, alert): self.alerts.append(alert)
    def snapshot(self): return {"accounts":list(self.accounts.values()),"alerts":list(self.alerts),"transactions":list(self.transactions)}
