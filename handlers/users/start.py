from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import keyb_main_menu
from loader import dp
from states.state_main_menu import MainMenu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! 🖐\n"
                         f"Бот поиска поездок BlaBlaCar, приветствует тебя!", reply_markup=keyb_main_menu.main_menu)
    await MainMenu.main_menu.set()
