import threading
from ingestion.base import EventSource
from live_stream import start_stream

class SyntheticEventSource(EventSource):
    def __init__(self, delay=1.0): self.delay=delay
    def start(self, on_account, on_transaction, stop_event=None):
        return start_stream(on_account,on_transaction,delay=self.delay,stop_event=stop_event or threading.Event())
