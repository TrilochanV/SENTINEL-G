# Security policy

## Sensitive data
Never commit real customer PII, bank credentials, API keys, account numbers or production transaction data.

## Before production
- Use a secret manager.
- Encrypt data in transit and at rest.
- Apply least-privilege RBAC.
- Add authentication and authorization to every API.
- Perform dependency and security scanning.
- Obtain legal/compliance approval for all data sources and automated decisions.
