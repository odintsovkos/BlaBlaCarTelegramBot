from aiogram.dispatcher import FSMContext

from keyboards.default import keyb_main_menu
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from states.state_main_menu import MainMenu


@dp.message_handler(Text(equals="Отмена"), state="*")
async def cancel_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=keyb_main_menu.main_menu)
    await MainMenu.main_menu.set()
