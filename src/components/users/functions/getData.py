from flask import request


def get_data_body():
    try:
        if request.is_json:
            user = request.json
        else:
            user = request.form
        return user

    except KeyError:
        return False
