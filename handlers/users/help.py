from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/menu - Вывести веню",
            "/help - Получить справку",
            "/info - Возможности бота")
    
    await message.answer("\n".join(text))
