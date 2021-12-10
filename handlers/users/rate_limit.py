from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from utils.misc import get_rate_limits


@dp.message_handler(Command("rate_limit"))
async def bot_rate_limit(message: types.Message):
    res = await get_rate_limits.request_rate_limits()
    await message.answer("Пока не работает =))")
    # await message.answer(f"Лимит запросов в день: {res['x-ratelimit-limit-day']}\n"
    #                      f"Осталось запросов в день: {res['x-ratelimit-remaining-day']}\n"
    #                      f"Лимит запросов в минуту: {res['x-ratelimit-limit-minute']}\n"
    #                      f"Осталось запросов в минуту: {res['x-ratelimit-remaining-minute']}")
