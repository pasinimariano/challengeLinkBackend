import uuid
from .store import users
from .functions.encripter import encrypt_password
from .functions.emailRegex import valid_email


def validate_username(username):
    response = 'Success'

    if len(username) < 3:
        response = 'The name must be at least 3 characters'
        return response

    for user in users:
        if username.lower() in user['username'].lower():
            response = 'Username already exist'
            break
        else:
            continue

    return response


def validate_email(email):
    response = 'Success'

    if not email:
        response = 'Email is required'
        return response

    if not valid_email(email):
        response = 'Invalid email'
        return response

    for user in users:
        if email.lower() in user['email'].lower():
            response = 'There is another user with that email'
            break
        else:
            continue

    return response


def create_user(username, email, password):
    id_generator = uuid.uuid1()
    username_validator = validate_username(username)
    email_validator = validate_email(email)
    password_encrypted = encrypt_password(password)

    if username_validator == 'Success' and email_validator == 'Success':
        users.append({
            'id': id_generator,
            'username': username,
            'email': email,
            'password': password_encrypted
        })
        return f'{username.upper()} was created successfully'
    else:
        bad_response = {
            "username": username_validator,
            "email": email_validator
        }
        return bad_response
