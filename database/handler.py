import sqlite3
import os


def create_file_directory(directory):
    """
    Creates a directory
    Arguments:
        directory - the directory to create
    """
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass


def create_file(file_name):
    """
    Creates a file
    Arguments:
        file_name - the name of the file to create
    """
    with open(file_name, 'w') as file:
        file.close()


def create_user_table():
    """
    Creates the user table
    """
    query = """
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(255) PRIMARY KEY NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            balance float NOT NULL DEFAULT 0,
            registered_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """
    # connect to db
    users_db, products_db = db_connect()
    cursor = users_db.cursor()
    cursor.execute(query)
    users_db.commit()
    users_db.close()


def create_products_table():
    """
    Creates the user table
    """
    query = """
        CREATE TABLE IF NOT EXISTS products (
            product_code VARCHAR(255) PRIMARY KEY NOT NULL,
            product_name VARCHAR(255) NOT NULL,
            product_price float NOT NULL DEFAULT 1.25,
            stock int NOT NULL DEFAULT 20
        );
    """
    # connect to products db
    users_db, products_db = db_connect()
    # Create the cursor
    cursor = products_db.cursor()
    cursor.execute(query)
    # Check if the database has any data in it. If not, add some.
    query = f"""
        SELECT * FROM products;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    if not data:
        # Insert multiple products
        query = f"""
            INSERT INTO products (product_code, product_name, product_price, stock)
            VALUES
                ('A1', 'Cola', 1.40, 20),
                ('A2', 'Orange', 1.20, 20),
                ('A3', 'Lemonade', 1.15, 20),
                ('A4', 'Milkshake', 2.50, 20),
                ('B1', 'Chocolate', 2.00, 20),
                ('B2', 'Crisps', 1.80, 20),
                ('B3', 'Brownie', 1.15, 20),
                ('B4', 'Cookie', 1.28, 20),
                ('C1', 'Apple', 1.29, 20),
                ('C2', 'Banana', 0.80, 20),
                ('C3', 'Strawberrys', 3, 20);
            """
        cursor.execute(query)
        products_db.commit()

    products_db.close()


def db_connect():
    """
    Connects to the database
    """
    try:
        # Connect to the databases
        users_db = sqlite3.connect('data/users.db')
        products_db = sqlite3.connect('data/products.db')
    except sqlite3.OperationalError:
        # If the databases don't exist, create them.
        create_file_directory('data')
        create_file('data/products.db')
        create_file('data/users.db')
        users_db = sqlite3.connect('data/users.db')
        products_db = sqlite3.connect('data/products.db')

    return users_db, products_db


def execute_query(query, db):
    """
    Executes a query
    Arguments:
        query - the query to execute
        db - the database to execute the query on ("users" or "products")
    """
    # Create tables if they don't exist
    create_products_table()
    create_user_table()
    # Connect to tables
    users_db, products_db = db_connect()
    # If the database doesn't exist at all, raise an error.
    if db != 'users' and db != 'products':
        raise ValueError('Invalid database')
    # Otherwise, set the cursor to the right database and execute the query.
    elif db == 'users':
        cursor = users_db.cursor()
        db = users_db
    elif db == 'products':
        cursor = products_db.cursor()
        db = products_db
    cursor.execute(query)
    # Fetch any results and return them.
    data = cursor.fetchall()
    # Commit changes and close the database.
    db.commit()
    db.close()
    # Return the results if they exist.
    if data:
        return data
    else:
        return None
