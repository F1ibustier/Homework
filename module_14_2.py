import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создайте таблицу Users

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# Заполните её 10 записями:

for i in range(1, 11):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                  (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

# Обновите balance у каждой 2-ой записи начиная с 1-ой на 500:
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, f'{i}'))

# Удалите каждую 3-ю запись в таблице начиная с 1-ой:

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}', ))

# Удалите из базы данных not_telegram.db запись с id = 6

cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчитать общее количество записей.

cursor.execute('SELECT COUNT(*) FROM Users')
# all_users = cursor.fetchone()[0]
# print(all_users)

# Посчитать сумму всех балансов.

cursor.execute('SELECT SUM(balance) FROM Users')
# all_balances = cursor.fetchone()[0]
# print(all_balances)

# Вывести в консоль средний баланс всех пользователей.

cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()
