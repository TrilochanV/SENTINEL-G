# SENTINEL-G Production Readiness Roadmap

## Completed in current upgrade
- Modular online behavioural profiling
- Device/IP/fingerprint correlation
- Incremental graph intelligence
- Unsupervised anomaly detection
- Risk fusion
- Transaction service boundary
- Event-source abstraction
- Synthetic and optional Kafka adapters
- Benchmark metrics
- Docker baseline
- Security guidance and environment separation

## Required before production
1. Authentication and RBAC
2. PostgreSQL persistence and migrations
3. Redis cache/hot-state adapter
4. Structured logging and monitoring
5. API schema validation and rate limiting
6. Integration tests and CI
7. Secret manager
8. Data retention and privacy controls
9. Independent model validation
10. Human approval before regulatory filing

## GNN milestone
Only begin after acquiring lawfully usable labelled transaction graph data. Add reproducible training, hold-out testing, calibration, drift monitoring and model versioning before claiming GNN-based detection.
