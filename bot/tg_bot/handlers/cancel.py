from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from ..handlers_repository import HandlersRepository as hr

__all__ = ["cancel"]


@hr.message_handler(commands=["cancel"], state="*", description="Cancel action")
async def cancel(message: Message, state: FSMContext):
    state_name = await state.get_state()
    await message.delete()
    await state.finish()

    if state_name:
        state_name = state_name.split(":", 1)[1]
        await message.answer(f"{state_name} canceled")
