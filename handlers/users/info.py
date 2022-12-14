from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from states.state_main_menu import MainMenu


@dp.message_handler(Command("info"), state=MainMenu.main_menu)
async def bot_info(message: types.Message):
    text = ("Этот бот ищет для Вас поездки по указанным данным на сайте BlaBlaCar\n"
            "Для того, чтобы получить все поездки в которых ещё остались места для бронирования, "
            "выберите пункт меню \"Поиск поездок\".\n "
            "Затем требуется отправить название города Отпраления и города Назначения.\n"
            "Так же можно отправить Геопозицию, нажав на скрепку, "
            "там выбрать точку на карте или сделать свайп вверх и в правом "
            "верхнем углу появится значок лупы, там можно ввести место и выбрать его из списка.\n"
            "После требуется ввести дату в соответствующем формате и время, пример будет в сообщении.\n"
            "Если поездки по указанным данным есть, то они появятся, каждая в отдельном сообщении.\n"
            "А так же под каждым "
            "сообщением с поездкой будут 2 кнопки, верхняя отправляет Вас на сайт BlaBlaCar и там Вы можете "
            "забронировать поездку, а нижняя отправляет Вас на сайт карт Google и Вы можете просмотреть маршрут, по "
            "которому вероятнее всего поедет водитель.\n")

    await message.answer(text)
