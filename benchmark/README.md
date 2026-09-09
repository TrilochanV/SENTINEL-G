# SENTINEL-G Benchmarking

Use a labelled held-out dataset. Never report accuracy alone for mule detection.

Required labels: `0=legitimate, 1=mule`.

Run:

```bash
python benchmark/evaluate.py --input data.csv --label label --score risk_score
```
