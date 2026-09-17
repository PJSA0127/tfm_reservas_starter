from __future__ import annotations

import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://tfm:tfm@localhost:5432/tfm_reservas",
    )
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "false").lower() == "true"
    WTF_CSRF_TIME_LIMIT = 3600


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = "test-only-secret"
    DATABASE_URL = os.getenv(
        "TEST_DATABASE_URL",
        "postgresql+psycopg://tfm:tfm@localhost:5432/tfm_reservas_test",
    )
    WTF_CSRF_ENABLED = False
