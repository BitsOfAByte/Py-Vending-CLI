import database.queries as db
import database.hashing as hasher
import database.validation as validator
import getpass as passinput

NEWLINES = "\n" * 35


def login_user():
    """
    Trigger an authentication check
    """
    authenticated = False
    tries = 0
    print(f"""{NEWLINES}
---------------------------------
         Login to Account
---------------------------------
""")
    while not authenticated:
        username = str(input("Enter your username > ").lower())
        password = hasher.hash_sha3_512(
            str(passinput.getpass("Enter your password > ")))

        if db.login_user(username, password):
            authenticated = True
            return username
        else:
            tries = tries + 1
            print(f"Incorrect Login [Try {tries}/3].\n")
            if tries == 3:
                return False


def register_user():
    """
    Registers a user.
    """
    print(f"""{NEWLINES}
---------------------------------
       Register an Account
---------------------------------
""")
    registered = False
    while not registered:
        username = str(input("Enter a username > ")).lower()
        password = hasher.hash_sha3_512(
            passinput.getpass("Enter a unique password > "))
        if validator.validate_username(username):
            registered = True
            db.create_user(username, password)
            print(
                f"{NEWLINES}Success: Account created, your account name is {username}.")
        else:
            print(validator.validate_username(username))
