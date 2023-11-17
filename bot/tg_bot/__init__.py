from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from .. import config
from .handlers import *  # don't remove. handlers won't be registered without this import
from .handlers_repository import HandlersRepository as hr


async def init_tg_bot():
    storage = RedisStorage2(config.REDIS_HOST, config.REDIS_PORT) if config.REDIS_HOST else MemoryStorage()
    bot = Bot(token=config.TG_API_TOKEN, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)
    await hr.register_handlers(dp)
    return dp
