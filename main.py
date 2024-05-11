# ============================================= SQL 11.05.24 l-53-54  ==================================================
import pymysql
from sql_queries import create_queries, delete_queries, get_queries, insert_queries, update_queries


server = 'localhost'
username = 'root'
port = 3306
passwd = ''
db = 'hospital_advanced'


if __name__ == '__main__':
    try:
        with pymysql.connect(host=server, port=port, user=username, password=passwd, database=db) as connection:
            print('Connected!')
            with connection.cursor() as cursor:
                while True:
                    print('1. Создать базу данных и переключиться на нее.')
                    print('2. Получить краткую информацию про отделения.')
                    print('3. Получить краткую информацию про отделения и палаты.')
                    print('4. Получить информацию по докторам и специализациям.')
                    print('5. Получить информацию по докторам и специализациям.')
                    print('6. Вывести все этажи без повторений, на которых располагаются палаты.')
                    print('7. Вывести с фондом финансирования в диапазоне.')
                    print('0. Выход.')
                    user_choice = input('Ваш выбор: ')
                    match user_choice:
                        case '1':
                            create_queries.create_database(cursor)
                        case '2':
                            get_queries.get_department_info(cursor)
                        case '3':
                            get_queries.get_departments_wards(cursor)
                        case '4':
                            get_queries.get_doctors_and_specializations(cursor)
                        case '5':
                            get_queries.get_doctors_and_phone(cursor)
                        case '6':
                            get_queries.get_all_departments_with_wards(cursor)
                        case '7':
                            get_queries.get_departments_with_financing_between(cursor)
                        case '0':
                            connection.close()
                            break
                        case _:
                            print('Неизвестная команда. Попробуйте еще.')

    except pymysql.Error as error:
        print(error)
