from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поиск поездок"),

        ],
        [
            KeyboardButton(text="Помощь"),
            KeyboardButton(text="Инфо о боте"),
        ],
    ],
    resize_keyboard=True
)
