from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.default import cancel
from loader import dp
from states.location import Locations


@dp.message_handler(Command(["search_trip"]))
async def show_menu(message: Message):
    await message.answer("Введите город отправления", reply_markup=cancel)
    await Locations.from_location.set()
