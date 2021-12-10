from psycopg2 import Error


def delete_all_data_from_table(cursor, *tables):
    try:
        insert_query = f""" TRUNCATE {', '.join(tables)} CASCADE """
        cursor.execute(insert_query)
    except (Exception, Error) as error:
        print('Ошибка при работе с PostgreSQL в функции delete_all_data_from_table', error)
