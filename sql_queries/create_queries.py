def create_database(cursor):
    cursor.execute('''CREATE DATABASE IF NOT EXISTS hospital_advanced''')
    cursor.execute('''USE hospital_advanced''')

# отделение
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS departments (
                    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    building INT NOT NULL CHECK(building BETWEEN 1 AND 5),
                    financing DECIMAL(10, 2) NOT NULL DEFAULT (0) CHECK(financing >= 0),
                    department_name VARCHAR(100) NOT NULL UNIQUE
                    )''')

    # заболевание
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS diseases (
                    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    disease_name VARCHAR(100) NOT NULL UNIQUE,
                    severity INT NOT NULL DEFAULT (1) CHECK(severity > 0),
                    department_id INT NOT NULL,
                    FOREIGN KEY (department_id) REFERENCES departments(id)
                    )''')

    # врачи
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS doctors (
                   id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                   first_name VARCHAR(100) NOT NULL,
                   last_name VARCHAR(100) NOT NULL,
                   phone VARCHAR(14),
                   salary DECIMAL(10, 2) NOT NULL CHECK(salary >= 0)
                    )''')

    # обследования, процедуры
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS examinations (
                   id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                   examination_name VARCHAR(100) NOT NULL UNIQUE,
                   day_of_week INT NOT NULL CHECK(day_of_week BETWEEN 1 AND 7),
                   start_time TIME NOT NULL CHECK(start_time >= '8:00' AND start_time < '18:00'),
                   end_time TIME NOT NULL CHECK(start_time < end_time)
                    )''')

    # палаты
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS wards (
                    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    ward_name VARCHAR(25) NOT NULL UNIQUE,
                    floor INT NOT NULL CHECK (floor > 0),
                    department_id INT NOT NULL,
                    FOREIGN KEY (department_id) REFERENCES departments(id)
                    )''')

    # связь Многие ко многим между врачами и обследованиями (сквозная таблица между таблицами)
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS doctors_and_examinations (
                    doctor_id INT NOT NULL,
                    examination_id INT NOT NULL,
                    PRIMARY KEY (doctor_id, examination_id),
                    FOREIGN KEY (doctor_id) REFERENCES doctors(id),
                    FOREIGN KEY (examination_id) REFERENCES examinations(id)
                    )''')

    # отпуска
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS vacations (
                    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    start_date DATE NOT NULL,
                    end_date DATE CHECK (end_date > start_date),
                    doctor_id INT NOT NULL,
                    FOREIGN KEY (doctor_id) REFERENCES doctors(id) 
                    )''')

    # специализации
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS specializations (
                    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    specialization_name VARCHAR(100) NOT NULL 
                    )''')

    # доктора и специализации (многие ко многим)
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS doctors_and_specializations (
                    doctor_id INT NOT NULL,
                    specialization_id INT NOT NULL, 
                    PRIMARY KEY (doctor_id, specialization_id),
                    FOREIGN KEY (doctor_id) REFERENCES doctors(id),
                    FOREIGN KEY (specialization_id) REFERENCES specializations(id)
                    )''')

    # спонсоры
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS sponsors (
                    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    sponsor_name VARCHAR(100) NOT NULL
                    )''')

    # пожертвования
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS donations (
                    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    summ_of_donate DECIMAL(10, 2) NOT NULL CHECK (summ_of_donate > 0),
                    sponsor_id INT NOT NULL,
                    department_id INT NOT NULL,
                    FOREIGN KEY (sponsor_id) REFERENCES sponsors(id),
                    FOREIGN KEY (department_id) REFERENCES departments(id)
                    )''')

    print('База данных больница и ее таблицы успешно созданы!!!')
