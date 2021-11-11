import database.handler as handler


def create_user(username, password):
    """
    Creates a user
    Arguments:
        username <str>: The username of the user
        password <str>: The password of the user
    """
    query = f"""
        INSERT INTO users (username, password_hash)
        VALUES ('{username}', '{password}');
    """
    return handler.execute_query(query, 'users')


def get_username(username):
    """
    Check if a username exists in the database already, used for validation on registration
    Arguments:
        username <str>: The username to validate
    returns:
        True: Username is already taken
        False: Username is not taken
    """
    query = f"""
        SELECT * from users
        WHERE username = '{username}';
    """
    return handler.execute_query(query, 'users')


def login_user(username, password):
    """
    Logs in a user
    Arguments:
        username <str>: The username of the user
        password <str>: The password of the user
    """
    query = f"""
        SELECT * FROM users
        WHERE username = '{username}' AND password_hash = '{password}';
    """
    return handler.execute_query(query, 'users')


def get_user_balance(username):
    """
    Gets the balance of a user
    Arguments:
        username <str>: The username of the user
    """
    query = f"""
        SELECT balance FROM users
        WHERE username = '{username}';
    """
    return handler.execute_query(query, 'users')


def modify_user_balance(username, new_balance):
    """
    Modifies the balance of a user
    Arguments:
        username <str>: The username of the user
        operator <str>: The operator to use
        amount <float>: The amount to modify the balance by
    """
    query = f"""
        UPDATE users
        SET balance = '{new_balance}'
        WHERE username = '{username}';
    """
    return handler.execute_query(query, 'users')


def delete_user(username):
    """
    Deletes a user
    Arguments:
        username <str>: The username of the user
    """
    query = f"""
        DELETE FROM users
        WHERE username = '{username}';
    """
    return handler.execute_query(query, 'users')


def get_all_products():
    """
    Gets all products
    """
    query = f"""
        SELECT * FROM products;
    """
    return handler.execute_query(query, 'products')


def modify_stock(product_id, new_stock):
    """
    Modifies the stock of a product
    Arguments:
        product_id <str>: The id of the product
        new_stock <int>: The new stock of the product
    """
    query = f"""
        UPDATE products
        SET stock = '{new_stock}'
        WHERE product_code = '{product_id}';
    """
    return handler.execute_query(query, 'products')


def restock_all_products():
    """
    Restocks all products
    """
    query = f"""
        UPDATE products
        SET stock = '{20}';
    """
    return handler.execute_query(query, 'products')
