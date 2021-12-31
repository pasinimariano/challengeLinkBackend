import uuid
from .store import users, NewUser


def create_user(username, email, password):
    id_generator = uuid.uuid1()
    new_user = NewUser(username, email, password)
    hashed_pwd = new_user.password_generator()

    if new_user.validate_username() == 'Success' and new_user.validate_email() == 'Success':
        users.append({
            'id': id_generator,
            'username': new_user.username,
            'email': new_user.email,
            'password': hashed_pwd
        })
        return f'{username.upper()} was created successfully'
    else:
        bad_response = {
            "username": new_user.validate_username(),
            "email": new_user.validate_email()
        }
        return bad_response
