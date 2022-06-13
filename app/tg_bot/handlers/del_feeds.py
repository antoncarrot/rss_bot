from typing import Dict

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.callback_data import CallbackData

from ..handlers_repository import HandlersRepository as hr

__all__ = ["del_feeds"]


del_feed_data = CallbackData("del_feed", "id")
del_feed_confirm_data = CallbackData("del_feed_confirm", "id")


def _get_feed_keyboard():
    buttons = [
        InlineKeyboardButton("❌ rss1", callback_data=del_feed_data.new(id="rss1")),
        InlineKeyboardButton("❌ rss2", callback_data=del_feed_data.new(id="rss2")),
        InlineKeyboardButton("❌ rss3", callback_data=del_feed_data.new(id="rss3")),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    keyboard.row(InlineKeyboardButton("✅ Done", callback_data="del_done"))
    return keyboard


@hr.message_handler(commands=["del"], state="*", description="Delete feeds")
async def del_feeds(message: Message, state: FSMContext):
    await message.delete()
    await state.finish()

    keyboard = _get_feed_keyboard()
    await message.answer("You have 3 feeds", reply_markup=keyboard)


@hr.callback_handler(state="*", text="del_done")
async def del_done(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.answer()


@hr.callback_handler(state="*", text="del_back")
async def del_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()

    keyboard = _get_feed_keyboard()
    await callback.message.answer("You have 3 feeds", reply_markup=keyboard)
    await callback.answer()


@hr.callback_handler(state="*", filters=[del_feed_data.filter()])
async def del_feed(callback: CallbackQuery, state: FSMContext, callback_data: Dict):
    await callback.message.delete()

    buttons = [
        InlineKeyboardButton("❌ Delete", callback_data=del_feed_confirm_data.new(id=callback_data["id"])),
        InlineKeyboardButton("↩️ Back", callback_data="del_back"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await callback.message.answer(f"Are you sure delete feed {callback_data['id']}", reply_markup=keyboard)

    await callback.answer()


@hr.callback_handler(state="*", filters=[del_feed_confirm_data.filter()])
async def del_feed_confirm(callback: CallbackQuery, state: FSMContext, callback_data: Dict):
    await callback.message.delete()

    keyboard = _get_feed_keyboard()
    await callback.message.answer("You have 3 feeds", reply_markup=keyboard)
    await callback.message.answer(f"Feed {callback_data['id']} deleted")

    await callback.answer()
