from psycopg2 import Error


def get_traveler_id_from_database(cursor, telegram_id):
    try:
        select_query = f"""SELECT id FROM traveler WHERE telegram_id = {telegram_id}"""
        cursor.execute(select_query)
        result = cursor.fetchone()
        if result is None:
            return result
        else:
            return result[0]
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции get_user_id_from_database", error)


def get_all_traveler_id_from_database(cursor):
    try:
        select_query = f"""SELECT telegram_id FROM traveler"""
        cursor.execute(select_query)
        result = cursor.fetchone()
        if result is None:
            return result
        else:
            return result
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции get_user_id_from_database", error)


def get_traveler_trips_id_from_database(cursor, traveler_id):
    try:
        select_query = f"""SELECT id FROM traveler_trips WHERE traveler_id = {traveler_id}"""
        cursor.execute(select_query)
        result = cursor.fetchone()
        return result[0]
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции get_traveler_trips_id_from_database", error)


def get_from_location_id_from_database(cursor):
    try:
        select_query_from_location = f"""SELECT id FROM from_location WHERE id = (select max(id) from from_location)"""
        cursor.execute(select_query_from_location)
        result_from_location = cursor.fetchone()
        return result_from_location[0]
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции get_location_ids_from_database", error)


def get_to_location_id_from_database(cursor):
    try:
        select_query_to_location = f"""SELECT id FROM to_location WHERE id = (select max(id) from to_location)"""
        cursor.execute(select_query_to_location)
        result_to_location = cursor.fetchone()
        return result_to_location[0]
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции get_location_ids_from_database", error)


def get_count_traveler_trips(cursor):
    try:
        select_min_id = f"""SELECT id FROM traveler_trips WHERE id = (select min(id) from traveler_trips)"""
        cursor.execute(select_min_id)
        result_min_id = cursor.fetchone()

        select_max_id = f"""SELECT id FROM traveler_trips WHERE id = (select max(id) from traveler_trips)"""
        cursor.execute(select_max_id)
        result_max_id = cursor.fetchone()

        return result_max_id - result_min_id
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL в функции get_count_traveler_trips", error)
