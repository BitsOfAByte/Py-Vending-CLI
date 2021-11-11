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


def create_text_file(file_name):
    """
    Creates a text file
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
    db = db_connect()
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    db.close()


def db_connect():
    """
    Connects to the database
    """
    try:
        db = sqlite3.connect('data/users.db')
    except sqlite3.OperationalError:
        create_file_directory('data')
        create_text_file('data/users.db')
        db = sqlite3.connect('data/users.db')

    return db


def execute_query(query):
    """
    Executes a query
    Arguments:
        query - the query to execute
    """
    create_user_table()
    db = db_connect()
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    if data:
        return data
    else:
        return None
