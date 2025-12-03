import sqlite3
import os


db_path = 'school.db'
sql_path = 'queries.sql'

# Подключаемся к БД
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Читаем файл
try:
    with open(sql_path, 'r', encoding='utf-8') as file:
        sql_script = file.read()

    # Выполняем весь скрипт
    cursor.executescript(sql_script)
    conn.commit()
    print("Успех! База данных school.db создана и запросы выполнены.")

    # Проверка выведем результаты последнего запроса про оценку < 80
    print("\nПроверка (студенты с оценкой < 80):")
    cursor.execute("""
        SELECT DISTINCT s.full_name
        FROM students s
        JOIN grades g ON s.id = g.student_id
        WHERE g.grade < 80;
    """)
    for row in cursor.fetchall():
        print(row)

except FileNotFoundError:
    print(f"ОШИБКА: Файл '{sql_path}' не найден. Убедитесь, что main.py и queries.sql лежат в одной папке.")
except sqlite3.Error as e:
    print(f"Ошибка при выполнении SQL: {e}")
finally:
    conn.close()