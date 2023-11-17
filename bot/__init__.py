import logging.config

import uvloop

from . import config

logging.config.dictConfig(config.LOGGING)
uvloop.install()
