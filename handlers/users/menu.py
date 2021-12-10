from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text
from states.location import Locations


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите действие для продолжения", reply_markup=menu)


@dp.message_handler(Text(equals=["Поиск поездок"]), state=None)
async def search_trips(message: Message):
    await message.answer("Введите город отправления", reply_markup=ReplyKeyboardRemove())
    await Locations.from_location.set()


@dp.message_handler(Text(equals=["Последний запрос"]))
async def five_recent_requests(message: Message):
    await message.answer("Эта функция пока не работает", reply_markup=ReplyKeyboardRemove())
