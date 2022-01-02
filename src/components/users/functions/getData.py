from flask import request


def get_data_body():
    try:
        if request.is_json:
            username = request.json['username']
            email = request.json['email']
            password = request.json['password']
        else:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

        return {
            'username': username,
            'email': email,
            'password': password
        }

    except KeyError:
        return False
