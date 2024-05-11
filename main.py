# ============================================= SQL 11.05.24 l-53-54  ==================================================
import pymysql
from sql_queries import create_queries, delete_queries, get_queries, insert_queries, update_queries


# документация и примеры использования запросов в MySQL
# https://www.w3scholls.com/mysql/func_mysql_dayofweek.asp

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
                    print('8. Вывести названия палат, расположенных в корпусах 4 и 5 на 1-м этаже..')
                    print('9. Вывести названия, корпуса и финансирования отделения.')
                    print('10. Вывести названия, корпуса и финансирования отделения.')
                    print('11. Вывести докторов ушедших в отпуск.')
                    print('12. Вывести докторов которые работаю только в рабочие дни.')
                    print('13. Вывести докторов используя фильтр LIKE.')
                    print('14. Добавить доктора.')
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
                        case '8':
                            get_queries.get_wards_on_1_floor_and_building_4_5(cursor)
                        case '9':
                            get_queries.get_info_from_3_or_6_building(cursor)
                        case '10':
                            get_queries.get_departments_with_some_sponsor(cursor)
                        case '11':
                            get_queries.get_doctors_with_vacations_last_month(cursor)
                        case '12':
                            get_queries.get_doctors_and_dep_with_exam_on_workdays(cursor)
                        case '13':
                            get_queries.get_doctors_with_some_name(cursor)
                        case '14':
                            get_queries.add_doctor(cursor, connection)
                        case '0':
                            connection.close()
                            break
                        case _:
                            print('Неизвестная команда. Попробуйте еще.')

    except pymysql.Error as error:
        print(error)
