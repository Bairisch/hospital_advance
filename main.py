# ============================================= SQL 11.05.24 l-53-54  ==================================================
import pymysql
from sql_queries import create_queries, delete_queries, get_queries, insert_queries, update_queries


server = 'localhost'
username = 'root'
port = 3306
passwd = ''
database = 'hospital'


if __name__ == '__main__':
    try:
        with pymysql.connect(host=server, port=port, user=username, password=passwd) as connection:
            print('Connected!')
            with connection.cursor() as cursor:
                while True:
                    print('1. Создать базу данных и переключиться на нее.')
                    user_choice = input('Ваш выбор: ')
                    match user_choice:
                        case '1':
                            create_queries.create_database(cursor)
                        case '0':
                            connection.close()
                        case _:
                            print('Неизвестная команда. Попробуйте еще.')

    except pymysql.Error as error:
        print(error)
