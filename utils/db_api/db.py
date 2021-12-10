import psycopg2
from psycopg2 import Error

from data import config
from . import insert_to_db
from . import select_from_db


def open_connect():
    try:
        conn = psycopg2.connect(user=config.DB_USER,
                                database=config.DB_NAME,
                                password=config.DB_PASSWORD,
                                host=config.DB_HOST,
                                port=config.DB_PORT)
        conn.autocommit = False
        cur = conn.cursor()

        return conn, cur
    except (Exception, Error) as error:
        print("Ошибка при подключении к базе данных,", error)


def insert_data_to_database(telegram_id, first_name, last_name, username, response_api):
    global connection, cursor
    try:
        connection, cursor = open_connect()

        database_traveler_id = select_from_db.get_traveler_id_from_database(cursor=cursor, telegram_id=telegram_id)
        if database_traveler_id is None:
            insert_to_db.insert_db_traveler_data(cursor=cursor, telegram_id=telegram_id, first_name=first_name,
                                                 last_name=last_name,
                                                 user_name=username)
            database_traveler_id = select_from_db.get_traveler_id_from_database(cursor=cursor, telegram_id=telegram_id)

        trips_count = len(response_api['trips'])
        insert_to_db.insert_db_traveler_trips_data(cursor=cursor, traveler_id=database_traveler_id,
                                                   link=response_api['link'], trips_count=trips_count)
        for i in range(trips_count):
            insert_to_db.insert_db_from_location(cursor=cursor,
                                                 date_time=response_api['trips'][i]['waypoints'][0]['date_time'],
                                                 city=response_api['trips'][i]['waypoints'][0]['place']['city'],
                                                 address=response_api['trips'][i]['waypoints'][0]['place']['address'],
                                                 latitude=response_api['trips'][i]['waypoints'][0]['place']['latitude'],
                                                 longitude=response_api['trips'][i]['waypoints'][0]['place'][
                                                     'longitude'])
            insert_to_db.insert_db_to_location(cursor=cursor,
                                               date_time=response_api['trips'][i]['waypoints'][1]['date_time'],
                                               city=response_api['trips'][i]['waypoints'][1]['place']['city'],
                                               address=response_api['trips'][i]['waypoints'][1]['place']['address'],
                                               latitude=response_api['trips'][i]['waypoints'][1]['place']['latitude'],
                                               longitude=response_api['trips'][i]['waypoints'][1]['place']['longitude'])
            database_traveler_trips_id = select_from_db.get_traveler_trips_id_from_database(cursor,
                                                                                            database_traveler_id)
            from_location_id = select_from_db.get_from_location_id_from_database(cursor)
            to_location_id = select_from_db.get_to_location_id_from_database(cursor)
            insert_to_db.insert_db_trip(cursor=cursor,
                                        traveler_trips_id=database_traveler_trips_id,
                                        link=response_api['trips'][i]['link'],
                                        from_location_id=from_location_id,
                                        to_location_id=to_location_id,
                                        price=response_api['trips'][i]['price']['amount'],
                                        distance=response_api['trips'][i]['distance_in_meters'],
                                        duration=response_api['trips'][i]['duration_in_seconds'])

            connection.commit()
    except (Exception, Error) as error:
        print("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
        connection.rollback()
    finally:
        if connection:
            cursor.close()
            connection.close()
