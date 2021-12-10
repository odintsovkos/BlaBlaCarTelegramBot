from aiogram import executor

from loader import dp
import middlewares, handlers
from utils.notify_admins import admins_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await admins_notify(dispatcher, "Бот Запущен")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

