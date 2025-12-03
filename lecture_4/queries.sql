---Создание таблицы students
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL CHECK (birth_year >= 1900)
);

--- Создание таблицы grades
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade BETWEEN 0 AND 100),
    FOREIGN KEY(student_id) REFERENCES students(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

--Вставка студентов
---Мы не указываем id, так как он AUTOINCREMENT
INSERT INTO students (full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- Вставка оценок
INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
    (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
    (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
    (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
    (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
    (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
    (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
    (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
    (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92);


--- Оптимизация создание индексов

-- Индекс для поиска по имени (ускоряет задачу 3: поиск Алисы Джонсон)
CREATE INDEX idx_student_name ON students(full_name);

-- Индекс для фильтрации по году рожденияускоряет задачу 5)
CREATE INDEX idx_birth_year ON students(birth_year);

-- Индекс для внешнего ключа (критически важен для всех JOIN-ов: задачи 3,4, 7, 8)
CREATE INDEX idx_grades_student_id ON grades(student_id);

-- Индекс для фильтрации и группировки по предметам (ускоряет задачу 6)
CREATE INDEX idx_subject ON grades(subject);

-- Индекс для поиска по оценкам (ускоряет задачу 8: поиск оценок < 80)
CREATE INDEX idx_grade ON grades(grade);




--Нахождение оценок студента Alice Johnson
SELECT s.full_name, g.grade FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

---Посчитать средний балл каждого студента

SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name;

--Студенты родившиеся после 2004

SELECT * FROM students WHERE birth_year > 2004;


----Список предметов со средним баллом

SELECT subject, AVG(grade) as average_sub FROM grades GROUP BY subject;

--- Топ 3 студента с высшими баллами
SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 3;

--- СТуденты у которых оценка ниже 80 по любому предмету
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;
