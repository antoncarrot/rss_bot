import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_BOT_ADMIN_ID = os.getenv("TG_BOT_ADMIN_ID")
TG_BOT_PRIVATE_MODE = os.getenv("TG_BOT_PRIVATE_MODE", True)

MINIFLUX_API_URL = os.getenv("MINIFLUX_API_URL")
MINIFLUX_USER = os.getenv("MINIFLUX_USER")
MINIFLUX_PSWD = os.getenv("MINIFLUX_PSWD")
MINIFLUX_API_TOKEN = os.getenv("MINIFLUX_API_TOKEN")

if (not MINIFLUX_USER and not MINIFLUX_PSWD) and not MINIFLUX_API_TOKEN:
    raise ValueError("Miniflux user/password or api token not set")

DEBUG = os.getenv("APP_DEBUG", False)

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
