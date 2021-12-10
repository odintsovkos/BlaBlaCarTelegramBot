from aiogram import types
from aiogram.dispatcher import FSMContext
import re
import datetime

from loader import dp
from states.location import Locations
from utils.misc.geocoder_api import request_geocoder_api
from utils.misc import blablacar_api, format_message_trips
from keyboards.default import cancel


@dp.message_handler(state=Locations.from_location, content_types=types.ContentTypes.TEXT)
async def answer_from_location(message: types.Message, state: FSMContext):
    answer = message['text']
    answer_list = await request_geocoder_api(answer)
    if answer_list:
        await state.update_data(answer1=answer_list)
        await message.answer("Введите город назначения", reply_markup=cancel)
        await Locations.next()
    else:
        await message.answer("Не удается найти данный город")


@dp.message_handler(state=Locations.to_location, content_types=types.ContentTypes.TEXT)
async def answer_to_location(message: types.Message, state: FSMContext):
    answer = message['text']
    answer_list = await request_geocoder_api(answer)
    if answer_list:
        await state.update_data(answer2=answer_list)
        date = str(datetime.date.today()).split('-')
        await message.answer("Напишите дату поездки в формате\n"
                             "ДД ММ ГГГГ\n"
                             f"Пример: {date[2]} {date[1]} {date[0]}", reply_markup=cancel)
        await Locations.next()
    else:
        await message.answer("Не удается найти данный город", reply_markup=cancel)


@dp.message_handler(state=Locations.date_trip)
async def answer_to_location(message: types.Message, state: FSMContext):
    answer = message.text
    if re.fullmatch(r"\d{2}\s\d{2}\s\d{4}", answer):
        await state.update_data(answer3=answer.split())
        time_and_time = str(datetime.datetime.today()).split()
        time = time_and_time[1].split(':')
        await message.answer("Напишите время поездки в формате\n"
                             "ЧЧ ММ\n"
                             f"Пример: {time[0]} {time[1]}",reply_markup=cancel)

        await Locations.next()
    else:
        await message.answer('Неверный ввод!', reply_markup=cancel)


@dp.message_handler(state=Locations.time_trip)
async def answer_to_location(message: types.Message, state: FSMContext):
    data = await state.get_data()  # Получаем данные из машины состояний aiogram
    from_location_data = data.get("answer1")
    to_location_data = data.get("answer2")
    date_data = data.get("answer3")
    time_data = message.text

    # Проверяем, введенное пользователем, время поездки на соответсвие шаблону
    if re.fullmatch(r"\d{2}\s\d{2}", time_data):
        # Делаем запрос к сервису BlaBkaCar с данными, которые ввел пользователь
        response_api, status = await blablacar_api.request_blablacar_api(from_location_data,
                                                                         to_location_data,
                                                                         date_data,
                                                                         time_data.split())

        # Проверка ответа от сервиса и отправка сообщений с поездками пользователю
        await format_message_trips.send_message(message, response_api, status)

        await state.finish()
    else:
        await message.answer('Неверный ввод!', reply_markup=cancel)
