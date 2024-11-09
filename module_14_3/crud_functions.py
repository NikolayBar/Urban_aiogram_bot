import sqlite3
def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL);''')

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL);""")

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    # connection.commit()
    connection.close()
    return all_products

if __name__ == '__main__':
    initiate_db()
    # connection = sqlite3.connect('database.db')
    # cursor = connection.cursor()
    # cursor.execute("DELETE FROM Products")
    # cursor.execute(f"""INSERT INTO Products (title, description, price)
    # VALUES
    # ('Продукт1', 'Описание 01', 100),
    # ('Продукт2', 'Описание 02', 200),
    # ('Продукт3', 'Описание 03', 300),
    # ('Продукт4', 'Описание 04', 400);""")
    #
    #
    # connection.commit()
    # connection.close()
