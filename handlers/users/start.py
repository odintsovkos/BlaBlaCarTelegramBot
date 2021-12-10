from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer("Чтобы узнать о возможностях бота, используй команду /info")
    await message.answer("Выбери действие для продолжения", reply_markup=menu)
