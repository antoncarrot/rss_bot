from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from ..handlers_repository import HandlersRepository as hr

__all__ = ["list_feeds"]


@hr.message_handler(commands=["list"], state="*", description="Show feeds")
async def list_feeds(message: Message, state: FSMContext):
    await message.delete()
    await state.finish()

    buttons = [
        InlineKeyboardButton("1 rss1", callback_data="list_done"),
        InlineKeyboardButton("2 rss2", callback_data="list_done"),
        InlineKeyboardButton("3 rss3", callback_data="list_done"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    keyboard.row(InlineKeyboardButton("✅ Done", callback_data="list_done"))
    await message.answer("You have 3 feeds", reply_markup=keyboard)


@hr.callback_handler(state="*", text="list_done")
async def list_done(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.answer()
