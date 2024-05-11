-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Май 11 2024 г., 18:41
-- Версия сервера: 10.4.20-MariaDB
-- Версия PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `hospital_advanced`
--

-- --------------------------------------------------------

--
-- Структура таблицы `departments`
--

CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `building` int(11) NOT NULL CHECK (`building` between 1 and 5),
  `financing` decimal(10,2) NOT NULL DEFAULT 0.00 CHECK (`financing` >= 0),
  `department_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `departments`
--

INSERT INTO `departments` (`id`, `building`, `financing`, `department_name`) VALUES
(1, 1, '158845.00', 'Хирургия'),
(2, 2, '250.40', 'Гинекология'),
(3, 3, '154500.00', 'Неврология'),
(4, 4, '12250.40', 'Кардиология'),
(5, 5, '250000.00', 'Педиатрия');

-- --------------------------------------------------------

--
-- Структура таблицы `diseases`
--

CREATE TABLE `diseases` (
  `id` int(11) NOT NULL,
  `disease_name` varchar(100) NOT NULL,
  `severity` int(11) NOT NULL DEFAULT 1 CHECK (`severity` > 0),
  `department_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `diseases`
--

INSERT INTO `diseases` (`id`, `disease_name`, `severity`, `department_id`) VALUES
(1, 'Плоскостопие', 1, 1),
(2, 'Молочница', 1, 2),
(3, 'Невроз', 4, 3),
(4, 'Сердечная недостаточность', 3, 4);

-- --------------------------------------------------------

--
-- Структура таблицы `doctors`
--

CREATE TABLE `doctors` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `phone` varchar(14) DEFAULT NULL,
  `salary` decimal(10,2) NOT NULL CHECK (`salary` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `doctors`
--

INSERT INTO `doctors` (`id`, `first_name`, `last_name`, `phone`, `salary`) VALUES
(1, 'Арнольд', 'Шварценеггер', '+110025030', '10000.00'),
(2, 'Жан-Клод', 'ван Дамм', '+1005780', '9000.00'),
(3, 'Дольф', 'Лунгрен', '+495201050', '8000.00'),
(4, 'Сильвестер', 'Сталлоне', '+1005780', '7000.00');

-- --------------------------------------------------------

--
-- Структура таблицы `doctors_and_departments`
--

CREATE TABLE `doctors_and_departments` (
  `doctor_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `doctors_and_departments`
--

INSERT INTO `doctors_and_departments` (`doctor_id`, `department_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

-- --------------------------------------------------------

--
-- Структура таблицы `doctors_and_examinations`
--

CREATE TABLE `doctors_and_examinations` (
  `doctor_id` int(11) NOT NULL,
  `examination_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `doctors_and_examinations`
--

INSERT INTO `doctors_and_examinations` (`doctor_id`, `examination_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

-- --------------------------------------------------------

--
-- Структура таблицы `doctors_and_specializations`
--

CREATE TABLE `doctors_and_specializations` (
  `doctor_id` int(11) NOT NULL,
  `specialization_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `doctors_and_specializations`
--

INSERT INTO `doctors_and_specializations` (`doctor_id`, `specialization_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

-- --------------------------------------------------------

--
-- Структура таблицы `donations`
--

CREATE TABLE `donations` (
  `id` int(11) NOT NULL,
  `summ_of_donate` decimal(10,2) NOT NULL CHECK (`summ_of_donate` > 0),
  `sponsor_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `donations`
--

INSERT INTO `donations` (`id`, `summ_of_donate`, `sponsor_id`, `department_id`) VALUES
(1, '100000.00', 1, 1),
(2, '200000.00', 2, 2),
(3, '300000.00', 3, 3),
(4, '400000.00', 4, 4);

-- --------------------------------------------------------

--
-- Структура таблицы `examinations`
--

CREATE TABLE `examinations` (
  `id` int(11) NOT NULL,
  `examination_name` varchar(100) NOT NULL,
  `day_of_week` int(11) NOT NULL CHECK (`day_of_week` between 1 and 7),
  `start_time` time NOT NULL CHECK (`start_time` >= '8:00' and `start_time` < '18:00'),
  `end_time` time NOT NULL CHECK (`start_time` < `end_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `examinations`
--

INSERT INTO `examinations` (`id`, `examination_name`, `day_of_week`, `start_time`, `end_time`) VALUES
(1, 'Обход', 1, '10:35:24', '11:40:00'),
(2, 'Процедуры', 2, '12:00:00', '13:00:00'),
(3, 'Прием пациентов', 3, '14:00:00', '17:30:00'),
(4, 'Лечение', 4, '12:00:00', '17:00:00');

-- --------------------------------------------------------

--
-- Структура таблицы `specializations`
--

CREATE TABLE `specializations` (
  `id` int(11) NOT NULL,
  `specialization_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `specializations`
--

INSERT INTO `specializations` (`id`, `specialization_name`) VALUES
(1, 'Хирург'),
(2, 'Гинеколог'),
(3, 'Кардиолог'),
(4, 'Невролог');

-- --------------------------------------------------------

--
-- Структура таблицы `sponsors`
--

CREATE TABLE `sponsors` (
  `id` int(11) NOT NULL,
  `sponsor_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `sponsors`
--

INSERT INTO `sponsors` (`id`, `sponsor_name`) VALUES
(1, 'Сбербанк'),
(2, 'Альфа-Банк'),
(3, 'Газпром'),
(4, 'Татнефть');

-- --------------------------------------------------------

--
-- Структура таблицы `vacations`
--

CREATE TABLE `vacations` (
  `id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL CHECK (`end_date` > `start_date`),
  `doctor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `vacations`
--

INSERT INTO `vacations` (`id`, `start_date`, `end_date`, `doctor_id`) VALUES
(1, '2024-05-11', '2024-05-24', 1),
(2, '2024-05-24', '2024-06-05', 2),
(3, '2024-06-06', '2024-06-20', 3),
(4, '2024-06-21', '2024-07-05', 4);

-- --------------------------------------------------------

--
-- Структура таблицы `wards`
--

CREATE TABLE `wards` (
  `id` int(11) NOT NULL,
  `ward_name` varchar(25) NOT NULL,
  `floor` int(11) NOT NULL CHECK (`floor` > 0),
  `department_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `wards`
--

INSERT INTO `wards` (`id`, `ward_name`, `floor`, `department_id`) VALUES
(1, '1A', 1, 1),
(2, '2B', 2, 2),
(3, '3C', 3, 3),
(4, '4D', 4, 4);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `department_name` (`department_name`);

--
-- Индексы таблицы `diseases`
--
ALTER TABLE `diseases`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `disease_name` (`disease_name`),
  ADD KEY `department_id` (`department_id`);

--
-- Индексы таблицы `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `doctors_and_departments`
--
ALTER TABLE `doctors_and_departments`
  ADD PRIMARY KEY (`doctor_id`,`department_id`),
  ADD KEY `department_id` (`department_id`);

--
-- Индексы таблицы `doctors_and_examinations`
--
ALTER TABLE `doctors_and_examinations`
  ADD PRIMARY KEY (`doctor_id`,`examination_id`),
  ADD KEY `examination_id` (`examination_id`);

--
-- Индексы таблицы `doctors_and_specializations`
--
ALTER TABLE `doctors_and_specializations`
  ADD PRIMARY KEY (`doctor_id`,`specialization_id`),
  ADD KEY `specialization_id` (`specialization_id`);

--
-- Индексы таблицы `donations`
--
ALTER TABLE `donations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sponsor_id` (`sponsor_id`),
  ADD KEY `department_id` (`department_id`);

--
-- Индексы таблицы `examinations`
--
ALTER TABLE `examinations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `examination_name` (`examination_name`);

--
-- Индексы таблицы `specializations`
--
ALTER TABLE `specializations`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `sponsors`
--
ALTER TABLE `sponsors`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `vacations`
--
ALTER TABLE `vacations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctor_id` (`doctor_id`);

--
-- Индексы таблицы `wards`
--
ALTER TABLE `wards`
  ADD PRIMARY KEY (`id`),
  ADD KEY `department_id` (`department_id`),
  ADD KEY `ward_name` (`ward_name`) USING BTREE;

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `departments`
--
ALTER TABLE `departments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `diseases`
--
ALTER TABLE `diseases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `doctors`
--
ALTER TABLE `doctors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `donations`
--
ALTER TABLE `donations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `examinations`
--
ALTER TABLE `examinations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `specializations`
--
ALTER TABLE `specializations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `sponsors`
--
ALTER TABLE `sponsors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `vacations`
--
ALTER TABLE `vacations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `wards`
--
ALTER TABLE `wards`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `diseases`
--
ALTER TABLE `diseases`
  ADD CONSTRAINT `diseases_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

--
-- Ограничения внешнего ключа таблицы `doctors_and_departments`
--
ALTER TABLE `doctors_and_departments`
  ADD CONSTRAINT `doctors_and_departments_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
  ADD CONSTRAINT `doctors_and_departments_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

--
-- Ограничения внешнего ключа таблицы `doctors_and_examinations`
--
ALTER TABLE `doctors_and_examinations`
  ADD CONSTRAINT `doctors_and_examinations_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
  ADD CONSTRAINT `doctors_and_examinations_ibfk_2` FOREIGN KEY (`examination_id`) REFERENCES `examinations` (`id`);

--
-- Ограничения внешнего ключа таблицы `doctors_and_specializations`
--
ALTER TABLE `doctors_and_specializations`
  ADD CONSTRAINT `doctors_and_specializations_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
  ADD CONSTRAINT `doctors_and_specializations_ibfk_2` FOREIGN KEY (`specialization_id`) REFERENCES `specializations` (`id`);

--
-- Ограничения внешнего ключа таблицы `donations`
--
ALTER TABLE `donations`
  ADD CONSTRAINT `donations_ibfk_1` FOREIGN KEY (`sponsor_id`) REFERENCES `sponsors` (`id`),
  ADD CONSTRAINT `donations_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

--
-- Ограничения внешнего ключа таблицы `vacations`
--
ALTER TABLE `vacations`
  ADD CONSTRAINT `vacations_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`);

--
-- Ограничения внешнего ключа таблицы `wards`
--
ALTER TABLE `wards`
  ADD CONSTRAINT `wards_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
