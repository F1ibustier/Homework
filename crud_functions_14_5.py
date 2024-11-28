import sqlite3

def initiate_db():
    connection = sqlite3.connect('database_users.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL);
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL);
    ''')
    connection.commit()

def check_db(id, title, description, price):
    connection = sqlite3.connect('database_users.db')
    cursor = connection.cursor()

    check_db = cursor.execute('SELECT * FROM Products WHERE title=?', (title,))
    if check_db.fetchone() is None:
        cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (f'{id}', f'{title}', f'{description}', f'{price}'))
    connection.commit()

def get_all_products():
    connection = sqlite3.connect('database_users.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products WHERE id > ?', (0,))
    connection.commit()
    return cursor.fetchall()


def add_user(username, email, age):
    connection = sqlite3.connect('database_users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', '1000'))
    connection.commit()

def is_include(username):
    connection = sqlite3.connect('database_users.db')
    cursor = connection.cursor()

    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    connection.commit()
    if check_user.fetchone() is None:
        return True
    else:
        return False


initiate_db()

check_db(1,'Продукт 1', 'описание 1', 100)
check_db(2,'Продукт 2', 'описание 2', 200)
check_db(3,'Продукт 3', 'описание 3', 300)
check_db(4, 'Продукт 4', 'описание 4', 400)
