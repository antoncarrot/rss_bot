import os

TG_API_TOKEN = os.getenv("TG_API_TOKEN")

DB_URI = os.getenv("DB_URI", "mongodb://app:app@127.0.0.1:27017")
DB_NAME = os.getenv("DB_NAME", "app")

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
