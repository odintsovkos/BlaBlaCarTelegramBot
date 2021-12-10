from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поиск поездок")
        ],
        [
            KeyboardButton(text="Последний запрос")
        ]
    ],
    resize_keyboard=True
)