from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("menu", "Показать меню"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("info", "Что делает бот"),
            types.BotCommand("rate_limit", "Вывод остатков по запросам")
        ]
    )
