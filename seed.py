from faker import Faker
import psycopg2
from psycopg2.extras import execute_values

db_params = {
    "host": "localhost",
    "database": "task_manager",
    "user": "postgres",
    "password": "password", 
    "port": 5433
}

fake = Faker()

try:

    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Генерація та вставка випадкових користувачів
    users_data = [(fake.name(), fake.email()) for _ in range(20)]
    execute_values(
        cur, "INSERT INTO users (fullname, email) VALUES %s", users_data
    )
    print(f"Додано {len(users_data)} користувачів.")

    # Отримання ідентифікаторів статусів
    cur.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cur.fetchall()]

    # Отримання ідентифікаторів користувачів
    cur.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]

    # Генерація та вставка випадкових завдань
    tasks_data = [
        (
            fake.sentence(),
            fake.paragraph(),
            fake.random_element(status_ids),
            fake.random_element(user_ids),
        )
        for _ in range(50)
    ]
    execute_values(
        cur,
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES %s",
        tasks_data,
    )
    print(f"Додано {len(tasks_data)} завдань.")

    conn.commit()
    print("Дані успішно додані до бази даних.")

except Exception as e:
    print(f"Помилка: {e}")

finally:
    if conn:
        cur.close()
        conn.close()