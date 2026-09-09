import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    environment: str = os.getenv("SENTINEL_ENV", "development")
    database_url: str = os.getenv("DATABASE_URL", "")
    redis_url: str = os.getenv("REDIS_URL", "")
    risk_high: float = float(os.getenv("RISK_HIGH", "0.75"))
    risk_medium: float = float(os.getenv("RISK_MEDIUM", "0.45"))

settings = Settings()
