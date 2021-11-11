import database.queries as database

def validate_username(username):
    if database.get_username(username):
        return 'Username taken.'
    elif len(username) > 12:
        return 'Username too long.'
    elif len(username) < 2:
        return 'Username too short.'
    else:
        return True