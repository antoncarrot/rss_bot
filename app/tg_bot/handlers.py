from aiogram.types import Message

from .. import config
from .handlers_repository import HandlersRepository as hr

__all__ = ["start"]


@hr.message_handler(commands=["start"], state="*")
async def start(message: Message):
    msg = f"Hello, {message.from_user.full_name}!\nThis is RSS feeds aggregator bot.\n"
    if config.DEBUG:
        msg = f"{msg}Chat id is {message.chat.id}"
    await message.answer(msg)
