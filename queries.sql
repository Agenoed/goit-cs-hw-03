-- 1. Отримати всі завдання певного користувача.
SELECT * FROM tasks WHERE user_id = 1;

-- 2. Вибрати завдання за певним статусом.
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Оновити статус конкретного завдання.
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 3;

-- 4. Отримати список користувачів, які не мають жодного завдання.
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 5. Додати нове завдання для конкретного користувача.
INSERT INTO tasks (title, description, status_id, user_id) VALUES
('Нове завдання', 'Опис нового завдання', (SELECT id FROM status WHERE name = 'new'), 5);

-- 6. Отримати всі завдання, які ще не завершено.
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- 7. Видалити конкретне завдання .
DELETE FROM tasks WHERE id = 2;

-- 8. Знайти користувачів з певною електронною поштою.
SELECT * FROM users WHERE email LIKE '%@example.com';

-- 9. Оновити ім'я користувача.
UPDATE users SET fullname = 'Нове ім''я' WHERE id = 4;

-- 10. Отримати кількість завдань для кожного статусу.
SELECT s.name, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
SELECT t.*
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- 12. Отримати список завдань, що не мають опису.
SELECT * FROM tasks WHERE description IS NULL OR description = '';

-- 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
SELECT u.fullname, t.*
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 14. Отримати користувачів та кількість їхніх завдань.
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;