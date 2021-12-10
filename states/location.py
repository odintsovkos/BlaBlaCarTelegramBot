from aiogram.dispatcher.filters.state import StatesGroup, State


class Locations(StatesGroup):
    from_location = State()
    to_location = State()
    date_trip = State()
    time_trip = State()
