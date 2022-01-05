from flask import jsonify, make_response
from .controller import create_user, user_login, api_token, delete_user,update_user
from .functions.getData import get_data_body


def user_controller(server):

    @server.route('/signup', methods=['POST'])
    def new_user():
        body = get_data_body()
        if not body:
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm = "Some fields are incorrect or missing"'}
            )
        else:
            response = create_user(body['username'], body['email'], body['password'])
            if response[0] == 'Errors':
                return make_response(
                    jsonify(response),
                    403,
                    {'WWW-Authenticate': 'Basic realm ="Error occurred"'}
                )
            else:
                return make_response(response, 200)

    @server.route('/login', methods=['POST'])
    def login():
        body = get_data_body()
        if not body:
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm ="Some fields are incorrect or missing"'}
            )
        else:
            response = user_login(body)
            if response == 'Invalid':
                return make_response(
                    'Could not verify',
                    403,
                    {'WWW-Authenticate': 'Basic realm = "User is invalid"'}
                )
            elif response == 'Incorrect':
                return make_response(
                    'Could not verify',
                    403,
                    {'WWW-Authenticate': 'Basic realm = "Incorrect password"'}
                )
            else:
                return make_response(response, 200)

    @server.route('/canipass', methods=['GET', 'POST'])
    @api_token
    def authorized():
        return make_response('True', 200)

    @server.route('/delete', methods=['GET', 'POST'])
    @api_token
    def delete():
        body = get_data_body()
        if not body:
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm ="Some fields are incorrect or missing"'}
            )
        else:
            response = delete_user(body)
            if response == 'Invalid':
                return make_response(
                    'Could not verify',
                    403,
                    {'WWW-Authenticate': 'Basic realm = "User is invalid"'}
                )
            elif response == 'Incorrect':
                return make_response(
                    'Could not verify',
                    403,
                    {'WWW-Authenticate': 'Basic realm = "Incorrect password"'}
                )
            else:
                return make_response(response, 200)

    @server.route('/update', methods=['GET', 'POST'])
    @api_token
    def update():
        body = get_data_body()
        if not body:
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm ="Some fields are incorrect or missing"'}
            )
        else:
            response = update_user(body)
            if response == 'Invalid':
                return make_response(
                    'Could not verify',
                    403,
                    {'WWW-Authenticate': 'Basic realm = "User is invalid"'}
                )
            elif response == 'Incorrect':
                return make_response(
                    'Could not verify',
                    403,
                    {'WWW-Authenticate': 'Basic realm = "Empty fields"'}
                )
            else:
                return make_response(response, 200)
