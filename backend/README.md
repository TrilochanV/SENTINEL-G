# Backend migration
The legacy root application remains supported during migration. New services belong here; business logic should not be duplicated in route handlers.

Target ownership:
- api/: HTTP/WebSocket transport
- services/: orchestration
- core/: reusable detection logic
- repositories/: persistence adapters
