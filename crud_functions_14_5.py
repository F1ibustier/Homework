import sqlite3
connection = sqlite3.connect('database_users.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL);
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL);
    ''')

def check_db(id, title, description, price):
    check_db = cursor.execute('SELECT * FROM Products WHERE title=?', (title,))
    if check_db.fetchone() is None:
        cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (f'{id}', f'{title}', f'{description}', f'{price}'))

def get_all_products():
    cursor.execute('SELECT * FROM Products WHERE id > ?', (0,))
    return cursor.fetchall()

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', '1000'))

def is_include(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        return True
    else:
        return False

initiate_db()

check_db(1,'Продукт 1', 'описание 1', 100)
check_db(2,'Продукт 2', 'описание 2', 200)
check_db(3,'Продукт 3', 'описание 3', 300)
check_db(4, 'Продукт 4', 'описание 4', 400)

connection.commit()
# connection.close()
