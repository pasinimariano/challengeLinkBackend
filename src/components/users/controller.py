import uuid
import jwt
from dotenv import dotenv_values
from functools import wraps
from flask import request, make_response
from datetime import datetime, timedelta
from .store import users, NewUser
from .functions.encripter import check_encrypted_password
from .functions.getUser import get_user

ENV = dotenv_values('.env')


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
        return ['Errors', bad_response]


def user_login(user_data):
    user = get_user(user_data, users)
    print(users)
    if len(user) == 0:
        return 'Invalid'
    elif user[0]['password'] and check_encrypted_password(user_data['password'], user[0]['password']):
        try:
            token = jwt.encode({
                'exp': datetime.utcnow() + timedelta(minutes=25),
                'iat': datetime.utcnow(),
                'sub': user[0]['username']
            },
                ENV['SECRET_KEY'],
                algorithm='HS256'
            )
            return {'Token': token}
        except Exception as error:
            return error
    else:
        return 'Incorrect'


def delete_user(user_data):
    user = get_user(user_data, users)

    if len(user) == 0:
        return 'Invalid'
    else:
        users.remove(user[0])
        return "{name} has been deleted".format(name=user[0]['username'])


def update_user(user_data):
    if user_data['username'] and user_data['email'] and user_data['password']:
        user = [x for x in users if user_data['id'] == x['id']]

        if len(user) == 0:
            return 'Invalid'
        else:
            user_index = users.index(user[0])
            users[user_index] = user_data
            return "{name} has been updated".format(name=user[0]['username'])


def api_token(func):
    @wraps(func)
    def token_required(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm = "Token is missing"'}
            )

        try:
            jwt.decode(token, ENV['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm = "Token expired, log in again"'}
            )
        except jwt.InvalidTokenError:
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm = "Invalid token. Please log in again"'}
            )

        return func(*args, **kwargs)

    return token_required
