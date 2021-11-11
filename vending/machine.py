import database.queries as queries

vending_options = [["A1", "Crisps", 1.25], ["A2", "Chocolate", 1.50], ["A3", "Water", 0.65]]

NEWLINES = "\n" * 35


def user_balance(uid):
    """
    Returns the user's balance.
    Arguments:
        uid: The user's ID.
    """
    return float(queries.get_user_balance(uid)[0][0])

def show_vending_options(uid):
    """
    This function shows the vending options in a table
    """
    print("\nVending Options")
    print("Code | Product | Price")
    for i in vending_options:
        if(i[2] <= user_balance(uid)):
            print(f"{i[0]}  |   {i[1]}  |   {i[2]}  | ✅")
        else:
            print(f"{i[0]}  |   {i[1]}  |   {i[2]}  | ❎")



def search_for_choice(choice):
    """
    Searches for the choice in the vending options.
    Arguments:
        choice: The choice to search for.
    """
    for i in vending_options:
        if i[0].lower() == choice.lower():
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
        return search_for_choice(choice)

def add_funds(uid):
    try:
        funds_to_add = float(input("How much money do you want to input? > "))
        if funds_to_add < 0:
            print("You cannot input a negative amount of money")
            add_funds(uid)
        else:
            queries.modify_user_balance(uid, user_balance(uid) + funds_to_add)
            print(f"{NEWLINES}You have added £{funds_to_add} to your balance. Your new balance is £{user_balance(uid)}")
            show_menu(uid)
    except ValueError:
        print("Invalid amount! Try again")
        add_funds(uid)

def begin_vending_sequence(uid):
    """
    Begins the vending sequence.
    Arguments:
        uid: The user's ID.
    """
    # First off, print out the items that are available
    # Honestly, if I wasn't to tired of making this project, I'd make all the items go into a database and then just print them out here.
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
                print(f"{NEWLINES}You have purchased {choice[1]} for £{choice[2]}. Your new balance is £{user_balance(uid)}")
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
            exit()
    except ValueError:
        print("Invald Choice! Try again\n")
        menu_choices()


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
[3] - Exit
""")

    menu_choices(uid)
