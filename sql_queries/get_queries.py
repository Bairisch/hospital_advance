import pymysql


def get_department_info(cursor):
    cursor.execute('''SELECT department_name, building, financing FROM departments''')
    for data in cursor:        # кортеж - кортежей
        # print(f'{i[1]}, {i[2]}; {i[3]};')
        print(f'Этаж: {data[1]}; Отделение: {data[0]}; Бюджет: {data[2]};')


# соединить таблицы (2 таблицы по указанным полям)
def get_departments_wards(cursor):
    cursor.execute('''SELECT d.department_name, d.financing, w.ward_name FROM departments d
                    JOIN wards w ON d.id = w.department_id
                    ORDER BY (d.department_name) ASC
    ''')
    for data in cursor:        # кортеж - кортежей
        # print(f'{i[1]}, {i[2]}; {i[3]};')
        print(f'Этаж: {data[2]}; Отделение: {data[0]}; Бюджет: {data[1]};')


def get_doctors_and_specializations(cursor):
    cursor.execute('''SELECT d.first_name, d.last_name, s.specialization_name FROM doctors_and_specializations d_a_s
                    JOIN doctors d ON d.id = d_a_s.doctor_id
                    JOIN specializations s ON s.id = d_a_s.specialization_id
    ''')
    for data in cursor:
        print(*data, sep='; ')
        # print(f'Этаж: {data[2]}; Отделение: {data[0]}; Бюджет: {data[1]};')


def get_doctors_and_phone(cursor):
    '''
    Вывести фамилии и телефоны всех врачей
    '''
    cursor.execute('''SELECT first_name, last_name, phone FROM doctors
    ''')
    for data in cursor:
        print(*data, sep='; ')
        # print(f'Этаж: {data[2]}; Отделение: {data[0]}; Бюджет: {data[1]};')


def get_all_departments_with_wards(cursor):
    '''
    3. Вывести все этажи без повторений, на которых располагаются палаты.
    DISTINCT - выводить только уникальные (floor)
    '''
    cursor.execute('''SELECT DISTINCT floor FROM departments d
                        JOIN wards w ON w.department_id = d.id
    ''')
    for i in cursor:
        print(*i, sep='; ')


def get_departments_with_financing_between(cursor):
    '''
    Вывести название отделений, расположенных в 3-м корпусе
    с фондом финансирования в диапазоне от 12000 до 15000
    '''
    cursor.execute('''SELECT * FROM departments
                    WHERE financing BETWEEN 100000 AND 300000 AND building = 3
    ''')
    for i in cursor:
        print(*i, sep='; ')
