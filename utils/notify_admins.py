import logging
from aiogram import Dispatcher
from data.config import ADMINS


async def admins_notify(dp: Dispatcher, message_admin):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, message_admin)
        except Exception as err:
            logging.exception(err)
