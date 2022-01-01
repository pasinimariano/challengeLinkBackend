def get_user(username, email, users):
    if username:
        user = [user for user in users if username == user['username']]
    elif email:
        user = [user for user in users if username == user['email']]
    else:
        user = 'Empty fields'

    return user
