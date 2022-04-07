from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.state_main_menu import MainMenu


@dp.message_handler(CommandHelp(), state=MainMenu.main_menu)
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/info - Возможности бота")
    
    await message.answer("\n".join(text))
