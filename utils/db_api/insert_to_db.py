from psycopg2 import Error


def insert_db_traveler_data(cursor,
                            telegram_id,
                            first_name,
                            last_name,
                            user_name):
    """Запись в базу данных информации о пользователе бота"""

    try:
        insert_query = f""" INSERT INTO traveler (telegram_id, first_name, last_name, username) VALUES (%s, %s, %s, %s)"""
        item_tuple = (telegram_id, first_name, last_name, user_name)
        cursor.execute(insert_query, item_tuple)
    except (Exception, Error) as error:
        print('Ошибка при работе с PostgreSQL в функции insert_db_traveler_data', error)


def insert_db_traveler_trips_data(cursor,
                                  traveler_id,
                                  link,
                                  trips_count):
    """Запись в базу данных информации о пользователе бота"""

    try:
        insert_query = f""" INSERT INTO traveler_trips (traveler_id, searche_link, trips_count) VALUES (%s, %s, %s)"""
        item_tuple = (traveler_id, link, trips_count)
        cursor.execute(insert_query, item_tuple)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции insert_db_traveler_trips_data", error)


def insert_db_from_location(cursor,
                            date_time,
                            city,
                            address,
                            latitude,
                            longitude):
    """Запись в базу данных информации о месте отправления"""

    try:
        insert_query = f""" INSERT INTO from_location (date_time, city, address, latitude, longitude) VALUES (%s, %s, %s, %s, %s)"""
        item_tuple = (date_time, city, address, latitude, longitude)
        cursor.execute(insert_query, item_tuple)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции insert_db_from_location", error)


def insert_db_to_location(cursor,
                          date_time,
                          city,
                          address,
                          latitude,
                          longitude):
    """Запись в базу данных информации о месте назначения"""

    try:
        insert_query = f""" INSERT INTO to_location (date_time, city, address, latitude, longitude) VALUES (%s, %s, %s, %s, %s)"""
        item_tuple = (date_time, city, address, latitude, longitude)
        cursor.execute(insert_query, item_tuple)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции insert_db_to_location", error)


def insert_db_trip(cursor,
                   traveler_trips_id,
                   link,
                   from_location_id,
                   to_location_id,
                   price,
                   distance,
                   duration):
    """Запись в базу данных информации о поездке"""

    try:
        insert_query = f""" INSERT INTO trip (traveler_trips_id, link, from_location_id, to_location_id, price, distance, duration) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        item_tuple = (traveler_trips_id, link, from_location_id, to_location_id, price, distance, duration)
        cursor.execute(insert_query, item_tuple)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции insert_db_trip", error)