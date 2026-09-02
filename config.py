import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(ENV_FILE, override=True)


class Config:
    SECRET_KEY = os.getenv("RESQNOW_SECRET_KEY", "dev-only-change-this-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///resqnow.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SAMESITE = "Lax"
    UPLOAD_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
    UPLOAD_MIME_TYPES = {"image/png", "image/jpeg", "image/webp"}
    RATELIMIT_DEFAULT = "200/day;60/hour;10/minute"
    RATELIMIT_STORAGE_URI = "memory://"
