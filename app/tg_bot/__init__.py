from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .. import config
from .handlers import *  # don't remove. handlers won't be registered without this import
from .handlers_repository import HandlersRepository as hr


async def init_tg_bot():
    storage = MemoryStorage()
    bot = Bot(token=config.TG_API_TOKEN, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)
    await hr.register_handlers(dp)
    return dp
