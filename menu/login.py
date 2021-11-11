from wrappers.authentication import login_user, register_user 
from vending.machine import show_menu

NEWLINES = "\n" * 35

def auth_options():
    """
    This function handles the menu choices.
    """
    try:
        choice = int(input('Choice > '))
        if choice == 1:
            user_login = login_user()
            if user_login != False:
                show_menu(user_login)
            else:
                print("You failed to authenticate")
                exit()
        elif choice == 2:
            register_user()
            auth_menu()
        elif choice == 3:
            exit()
    except ValueError:
        auth_options()

def auth_menu():
    """
    Show a CLI menu to authenticate users
    """

    print(f"""{NEWLINES}
---------------------------------
       Authentication Menu
---------------------------------

[1] Login
[2] Register
[3] Quit
""")
    auth_options()