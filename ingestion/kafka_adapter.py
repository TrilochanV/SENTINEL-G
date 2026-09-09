"""Optional Kafka adapter; install confluent-kafka or kafka-python in deployment.
No bank credentials or topics are hard-coded here."""
from ingestion.base import EventSource

class KafkaEventSource(EventSource):
    def __init__(self, bootstrap_servers, topic, group_id="sentinel-g"):
        self.bootstrap_servers=bootstrap_servers; self.topic=topic; self.group_id=group_id
    def start(self, on_account, on_transaction, stop_event=None):
        try:
            from confluent_kafka import Consumer
        except ImportError as exc:
            raise RuntimeError("Install confluent-kafka to enable Kafka ingestion") from exc
        import json
        c=Consumer({"bootstrap.servers":self.bootstrap_servers,"group.id":self.group_id,"auto.offset.reset":"latest"})
        c.subscribe([self.topic])
        try:
            while not (stop_event and stop_event.is_set()):
                msg=c.poll(1.0)
                if msg is None: continue
                if msg.error(): continue
                event=json.loads(msg.value().decode("utf-8")); on_transaction(event)
        finally: c.close()
