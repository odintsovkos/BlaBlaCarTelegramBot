from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals="Отмена"), state="*")
async def cancel_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=ReplyKeyboardRemove())
    await message.answer("Список команд:\n"
                         "/start - Запустить бота\n"
                         "/search_trip - Поиск поездки\n"
                         "/help - Справка\n"
                         "/info - Информация о боте")
