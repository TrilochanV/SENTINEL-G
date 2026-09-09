# SENTINEL-G Target Architecture

## Detection flow

Transaction event → feature extraction → behavioural profiler + device intelligence + graph intelligence + anomaly detection + legacy AML engines → risk fusion → explainability/case workflow.

## Production adapters

The core pipeline is intentionally transport-agnostic. Implement bank ingestion through adapters such as Kafka, REST/webhooks, or approved CBS streams without changing detection logic.

## Important limitation

GNN training/inference is not claimed as implemented in this upgrade. It requires labelled graph datasets, PyTorch/PyG dependency management, reproducible training and validation before production use.
