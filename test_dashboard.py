#!/usr/bin/env python
"""Test dashboard endpoint."""
import sys
import time
sys.path.insert(0, '.')
from app import app

print('Testing dashboard endpoint...')
with app.test_client() as client:
    start = time.time()
    resp = client.get('/api/dashboard')
    elapsed = time.time() - start
    print(f'Status: {resp.status_code} (took {elapsed:.2f}s)')
    if resp.status_code == 200:
        data = resp.get_json() if hasattr(resp, 'get_json') else {}
        print(f'[ok] Response keys: {list(data.keys())[:10]}...')
    else:
        print(f'[error] {resp.data.decode()[:300]}')