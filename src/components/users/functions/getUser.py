def get_user(user, users):
    if "username" in user.keys():
        user = [x for x in users if user['username'] == x['username']]
    elif "email" in user.keys():
        user = [x for x in users if user['email'] == x['email']]
    elif "id" in user.keys():
        user = [x for x in users if user['id'] == x['id']]
    else:
        user = 'Empty fields'

    return user
