from abc import ABC, abstractmethod

class EventSource(ABC):
    """Transport boundary: Kafka, webhook, CBS and synthetic sources implement this."""
    @abstractmethod
    def start(self, on_account, on_transaction, stop_event=None): ...
