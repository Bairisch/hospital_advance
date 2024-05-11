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
                    ORDER BY w.ward_name ASC
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
    cursor.execute('''SELECT department_name, financing FROM departments
                    WHERE financing BETWEEN 100000 AND 300000 AND building = 3
    ''')
    for data in cursor:
        print(f'Название: {data[0]}; Финансирование: {data[1]};')


def get_wards_on_1_floor_and_building_4_5(cursor):
    '''
    Вывести названия палат, расположенных в корпусах 4 и 5 на 1-м этаже.
    '''
    cursor.execute('''SELECT * FROM departments d
                    JOIN wards w ON w.department_id = d.id
                    WHERE building BETWEEN 4 AND 5 AND floor = 1
    ''')
    for i in cursor:
        print(*i, sep='; ')


def get_info_from_3_or_6_building(cursor):
    '''
    Вывести названия, корпуса и финансирования отделения, расположенных в корпусах 3 или 5
    и имеющих фонд финансирования меньше 100 000 или больше 200 000.
    '''
    cursor.execute('''SELECT department_name, building, financing FROM departments
                    WHERE (financing < 100000 OR financing > 200000)
                    AND (building = 3 OR building = 5)
    ''')
    # то же самое
    # cursor.execute('''SELECT * FROM departments
    #                     WHERE financing NOT BETWEEN 100000 AND 300000
    #     ''')
    for i in cursor:
        print(*i, sep='; ')


def get_departments_with_some_sponsor(cursor):
    '''
    Вывести название отделения без повторения, которые спонсируются компанией название компаний
    '''
    cursor.execute('''SELECT DISTINCT department_name, summ_of_donate FROM departments dep
                    JOIN donations don ON dep.id = don.department_id
                    JOIN sponsors sp ON sp.id = don.sponsor_id
                    WHERE sponsor_name = 'Альфа-Банк'
    ''')
    for i in cursor:
        print(*i, sep='; ')


def get_doctors_with_vacations_last_month(cursor):
    '''

    '''
    cursor.execute('''SELECT doc.first_name, doc.last_name, start_date, end_date FROM doctors doc
                    JOIN vacations vac ON vac.doctor_id = doc.id
                    WHERE start_date >= DATE_SUB(NOW(), INTERVAL 1 MONTH) AND start_date <= NOW()
    ''')
    for i in cursor:
        print(*i, sep='; ')


def get_doctors_and_dep_with_exam_on_workdays(cursor):
    '''

    '''
    cursor.execute('''SELECT * FROM departments dep
                      JOIN doctors_and_departments d_a_d ON d_a_d.department_id = dep.id
                      JOIN doctors doc ON d_a_d.doctor_id = doc.id
                      JOIN doctors_and_examinations d_a_e ON d_a_e.doctor_id = doc.id
                      JOIN examinations exam ON d_a_e.examination_id = exam.id
                      WHERE day_of_week BETWEEN 1 AND 5
                      
       ''')
    for i in cursor:
        print(*i, sep='; ')

