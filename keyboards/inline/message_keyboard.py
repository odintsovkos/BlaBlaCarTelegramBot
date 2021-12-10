from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_inline_keyboard(num, response_api):
    from_latitude = response_api['waypoints'][0]['place']['latitude']
    from_longitude = response_api['waypoints'][0]['place']['longitude']
    to_latitude = response_api['waypoints'][1]['place']['latitude']
    to_longitude = response_api['waypoints'][1]['place']['longitude']

    url_maps = f"https://www.google.com/maps/dir/?api=1&origin={from_latitude},{from_longitude}&" \
               f"destination={to_latitude},{to_longitude}&" \
               f"travelmode=driving"

    link = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Открыть поездку',
                                     url=response_api['link'])
            ],
            [
                InlineKeyboardButton(text='Маршрут на карте',
                                     url=url_maps)
            ]
        ]
    )
    return link
