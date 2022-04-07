from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from handlers.users.help import bot_help
from handlers.users.info import bot_info
from keyboards.default import cancel
from loader import dp
from states.location import Locations
from states.state_main_menu import MainMenu


@dp.message_handler(Command(["search_trip"]), state=MainMenu.main_menu)
async def show_menu(message: Message):
    await message.answer("Введите город отправления", reply_markup=cancel.cancel)
    await Locations.from_location.set()


@dp.message_handler(state=MainMenu.main_menu)
async def main_manu(message: types.Message):
    answer = message['text']
    if answer == "Поиск поездок":
        await message.answer("Введите город отправления", reply_markup=cancel.cancel)
        await Locations.from_location.set()
    elif answer == "Помощь":
        await bot_help(message)
    elif answer == "Инфо о боте":
        await bot_info(message)

