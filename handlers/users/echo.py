from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await dp.bot.delete_message(message.chat.id, message.message_id)
    await dp.bot.send_message(message.chat.id, "Такой команды не найдено!\n"
                                               "Список команд:\n"
                                               "/start - Запустить бота\n"
                                               "/search_trip - Поиск поездки\n"
                                               "/help - Справка\n"
                                               "/info - Информация о боте")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await dp.bot.delete_message(message.chat.id, message.message_id)
    await dp.bot.send_message(message.chat.id, "Такой команды не найдено!\n"
                                               "Список команд:\n"
                                               "/start - Запустить бота\n"
                                               "/search_trip - Поиск поездки\n"
                                               "/help - Справка\n"
                                               "/info - Информация о боте")
