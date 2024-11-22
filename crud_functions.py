import sqlite3

connection = sqlite3.connect('database_products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL)
    ''')

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

initiate_db()

for i in range(1, 5):
    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)',
                   (f'{i}', f'Продукт {i}', f'Описание {i}', f'{i*100}'))

connection.commit()
# connection.close()
