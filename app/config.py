import os

TG_API_TOKEN = os.getenv("TG_API_TOKEN")

DB_USER = os.getenv("DB_USER", "app")
DB_PASS = os.getenv("DB_PASS", "app")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", 27017)
DB_NAME = os.getenv("DB_NAME", "app")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

DEBUG = True if os.getenv("DEBUG") else False

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s.%(funcName)s:%(lineno)s %(message)s"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"verbose": {"format": LOG_FORMAT}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "verbose"}},
    "root": {
        "level": "DEBUG" if DEBUG else "INFO",
        "handlers": ["console"],
    },
}
