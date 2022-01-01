import uuid
import jwt
from datetime import datetime, timedelta
from .store import users, NewUser
from .functions.encripter import check_encrypted_password
from .functions.getUser import get_user


def create_user(username, email, password):
    id_generator = uuid.uuid1().hex
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


def user_login(username, email, password, secret_key):
    user = get_user(username, email, users)

    if len(user) == 0:
        return {'Error': f'User {username} not found'}
    elif user[0]['password'] and check_encrypted_password(password, user[0]['password']):
        token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(minutes=25),
            'iat': datetime.utcnow(),
            'sub': user[0]['username']
        },
            secret_key,
            algorithm='HS256'
        )

        return {'Token': token}
    else:
        return {'Unable to verify, incorrect password', 403, {'WWW-Authenticate': 'Basic real:' "Authentication fails"}}
