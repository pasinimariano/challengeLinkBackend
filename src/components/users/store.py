from .functions.emailRegex import valid_email
from .functions.encripter import encrypt_password

users = []


class NewUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def validate_username(self):
        response = 'Success'

        if len(self.username) < 3:
            response = 'The name must be at least 3 characters'
            return response

        for user in users:
            if self.username.lower() == user['username'].lower():
                response = 'Username already exist'
                break
            else:
                continue

        return response

    def validate_email(self):
        response = 'Success'

        if not self.email:
            response = 'Email is required'
            return response

        if not valid_email(self.email):
            response = 'Invalid email'
            return response

        for user in users:
            if self.email.lower() == user['email'].lower():
                response = 'There is another user with that email'
                break
            else:
                continue

        return response

    def password_generator(self):
        return encrypt_password(self.password)

    def __str__(self):
        return ''


