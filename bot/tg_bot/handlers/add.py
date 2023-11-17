from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from ..handlers_repository import HandlersRepository as hr
from ._states import ManageAddStatesGroup

__all__ = ["add"]


@hr.message_handler(commands=["add"], state="*", description="Add feed")
async def add(message: Message, state: FSMContext):
    await message.delete()
    await state.finish()

    await message.answer("Enter feed url")
    await ManageAddStatesGroup.add_feed.set()


@hr.message_handler(state=ManageAddStatesGroup.add_feed)
async def add_feed_state(message: Message, state: FSMContext):
    if not message.text.lower().startswith("https://"):
        await message.reply("Not valid url")
        return

    await message.reply(f"Feed added {message.text.lower()}")
    await state.finish()
