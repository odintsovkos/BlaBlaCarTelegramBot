from aiogram.types import Message, ReplyKeyboardRemove
from utils.db_api import db
from keyboards.inline import message_keyboard
from loader import dp
from utils.notify_admins import admins_notify
import datetime


def title_message(count):
    if count == 1:
        count = "одна"
        text = f"<u>Найдена {count} доступная поездка</u>🔍"
    elif 5 <= count <= 20:
        text = f"<u>Найдено {count} доступных поездок</u>🔍"
    else:
        text = f"<u>Найдено {count} доступных поездки</u>🔍"
    return text


def trip_message(num, response_api):
    from_location = response_api['waypoints'][0]['place']['city']
    to_location = response_api['waypoints'][1]['place']['city']
    distance = int(response_api['distance_in_meters'] / 1000)
    time_to_go = response_api['waypoints'][0]['date_time'].split('T')[1][:5]
    time_to_end = response_api['waypoints'][1]['date_time'].split('T')[1][:5]
    price = response_api['price']['amount'].split('.')[0]
    try:
        auto = f"{response_api['vehicle']['make']} {response_api['vehicle']['model']}"
    except Exception:
        auto = "Автомобиль не указан"

    text = f"<u><b>Поездка №{num + 1}</b></u>🚌\n" \
           f"<i><b>{from_location} --> {to_location}, {distance} км</b></i>\n" \
           f"<code>Отправление в</code> {time_to_go}\n" \
           f"<code>Прибытие в</code> {time_to_end}\n" \
           f"<code>Стоимость:</code> <b>{price}</b> руб.\n" \
           f"<code>Автомобиль:</code>\n" \
           f"{auto}"

    return text


async def validation_response(message, response_api, status):
    if status == 200:
        # Проверяем в ответе сервиса, есть ли поездки
        if response_api['search_info']['count'] > 0:
            return True
        # Уведомление пользователя о том, что Поездки не найдены
        else:
            await message.answer("Поездок на эти данные не найдено")

            await admins_notify(dp, f'{message.from_user.id}, {message.from_user.username}\n'
                                    f'[INFO] Поездки не найдены'
                                    f'Time: {datetime.datetime.now()}')
            return False

    # Status code не 200, уведомляем пользователя о том что произошла ошибка получения данных из сервиса
    else:
        await message.answer("Ошибка при получении данных от сервиса BlaBlaCar")
        print(f"Status code: {status}\n", response_api)

        await admins_notify(dp, f'{message.from_user.id}, {message.from_user.username}\n'
                                f'[ERROR] Server response status code {status}\n'
                                f'Time: {datetime.datetime.now()}')
        return False


async def preparation_message(message: Message, response_api_list, status):
    trips_list = []
    for response in response_api_list:
        if await validation_response(message, response, status):
            db.insert_data_to_database(message.from_user.id,
                                       message.from_user.first_name,
                                       message.from_user.last_name,
                                       message.from_user.username,
                                       response)
            for trip_num in range(len(response['trips'])):
                trips_list.append(response['trips'][trip_num])
    return trips_list


async def send_message(message, response_api_list, status):
    trips = await preparation_message(message, response_api_list, status)
    # Отправка пользователю сообщения с информацией о количестве найденных поездок
    await message.answer(title_message(len(trips)))

    # Отправка сообщений пользователю с поездками
    for num in range(len(trips)):
        await message.answer(trip_message(num, trips[num]),
                             reply_markup=message_keyboard.create_inline_keyboard(num, trips[num]))

    await message.answer("Спасибо за то, что воспользовались данным Ботом", reply_markup=ReplyKeyboardRemove())
