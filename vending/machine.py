import database.queries as queries

NEWLINES = "\n" * 35


def user_balance(uid):
    """
    Returns the user's balance.
    Arguments:
        uid: The user's ID.
    """
    return round(float(queries.get_user_balance(uid)[0][0]), 2)


def show_vending_options(uid):
    """
    This function shows the vending options in a table
    """
    VENDING_OPTIONS = queries.get_all_products()
    available_items = ''
    for i in VENDING_OPTIONS:
        if(i[2] >= user_balance(uid)):
            pass
        elif i[3] == 0:
            available_items += f"{i[0]}: {i[1]} - Out of Stock\n"
        else:
            available_items = available_items + \
                f"{i[0]}  |   {i[1]} costing £{i[2]} - In stock ({i[3]})\n"
    if available_items:
        print(f"""
--------------------------------
        Vending Options
--------------------------------
""")
        print(available_items)
    else:
        print(
            f"{NEWLINES}Attention: You cannot afford anything! Add some money and come back.")
        show_menu(uid)


def search_for_choice(uid, choice):
    """
    Searches for the choice in the vending options.
    Arguments:
        choice: The choice to search for.
    """
    VENDING_OPTIONS = queries.get_all_products()
    for i in VENDING_OPTIONS:
        if i[0].lower() == choice.lower():
            if i[3] == 0:
                print(f"{NEWLINES}Sorry, {i[1]}' is out of stock.")
                begin_vending_sequence(uid)
            return i


def handle_choice(uid):
    """
    This function handles the choice of the user.
    """
    print("Type 'Back' to go back.")
    choice = input("Enter Code > ")
    if choice.lower() == "back":
        show_menu(uid)
    else:
        return search_for_choice(uid, choice)


def add_funds(uid):
    try:
        funds_to_add = float(input("How much money do you want to input? > "))
        if funds_to_add < 0:
            print("Sorry! You cannot input a negative amount of money")
            add_funds(uid)
        else:
            queries.modify_user_balance(uid, user_balance(uid) + funds_to_add)
            print(
                f"{NEWLINES}Success: You have added £{funds_to_add} to your balance. Your new balance is £{user_balance(uid)}")
            show_menu(uid)
    except ValueError:
        print("That doesn't look valid! Try again.")
        add_funds(uid)


def begin_vending_sequence(uid):
    """
    Begins the vending sequence.
    Arguments:
        uid: The user's ID.
    """
    # First off, print out the items that are available
    show_vending_options(uid)
    # Next off, make the user pick from the options
    chosen = False
    while not chosen:
        choice = handle_choice(uid)
        if choice:
            chosen = True
            # Now we need to check if the user has enough money to buy the item
            if user_balance(uid) >= choice[2]:
                # If they do, we need to update the database
                queries.modify_user_balance(uid, user_balance(uid) - choice[2])
                queries.modify_stock(choice[0], choice[3] - 1)
                print(
                    f"{NEWLINES}You have purchased {choice[1]} for £{choice[2]}. Your new balance is £{user_balance(uid)}")
                show_menu(uid)
            else:
                print(f"{NEWLINES}You don't have enough money to buy that item")
                begin_vending_sequence(uid)
        else:
            print("Invalid choice")


def menu_choices(uid):
    try:
        option = int(input("Choice > "))
        if option == 1:
            begin_vending_sequence(uid)
        elif option == 2:
            add_funds(uid)
        elif option == 3:
            print(f"{NEWLINES} Restocked all products!")
            queries.restock_all_products()
            show_menu(uid)
        elif option == 4:
            print(f"Thank you for using the vending machine, {uid}.")
            exit()
    except ValueError:
        print("Invald Choice! Try again\n")
        menu_choices(uid)


def show_menu(uid):
    """
    Shows the user the menu.
    Arguments:
        uid: The user's ID.
    """
    print(
        f"""
--------------------------------
      Vending Machine Menu
--------------------------------
Logged in as: {uid} | Balance: £{user_balance(uid)}

[1] - Make a purchase
[2] - Input money
[3] - Restock All Items
[4] - Exit
""")

    menu_choices(uid)
