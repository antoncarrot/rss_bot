from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from ..handlers_repository import HandlersRepository as hr

__all__ = ["start"]


@hr.message_handler(commands=["start"], state="*")
async def start(message: Message, state: FSMContext):
    await message.delete()
    await state.finish()

    msg = f"Hello, {message.from_user.full_name}!\nThis is RSS feeds aggregator bot.\n"
    await message.answer(msg)
