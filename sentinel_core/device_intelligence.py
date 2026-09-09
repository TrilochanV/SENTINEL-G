from collections import defaultdict

class DeviceIntelligence:
    """Entity resolution across account, device, IP and optional fingerprint."""
    def __init__(self):
        self.device_accounts=defaultdict(set); self.ip_accounts=defaultdict(set); self.fp_accounts=defaultdict(set)
    def observe(self, account_id, device_id=None, ip_address=None, fingerprint=None):
        if device_id: self.device_accounts[device_id].add(account_id)
        if ip_address: self.ip_accounts[ip_address].add(account_id)
        if fingerprint: self.fp_accounts[fingerprint].add(account_id)
    def score(self, account_id, device_id=None, ip_address=None, fingerprint=None):
        sizes=[]
        if device_id: sizes.append(len(self.device_accounts[device_id]))
        if ip_address: sizes.append(len(self.ip_accounts[ip_address]))
        if fingerprint: sizes.append(len(self.fp_accounts[fingerprint]))
        shared=max(sizes, default=1)
        return min(1.0, max(0.0, (shared-1)/9.0))
