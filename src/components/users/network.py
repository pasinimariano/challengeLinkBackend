from flask import request, jsonify
from .controller import create_user, user_login
from .functions.getData import get_data_body


def user_controller(server, secret_key):

    @server.route('/createuser', methods=['POST'])
    def new_user():
        body = get_data_body()
        response = create_user(body['username'], body['email'], body['password'])

        return jsonify(response)

    @server.route('/login', methods=['POST'])
    def login():
        body = get_data_body()
        response = user_login(body['username'], body['email'], body['password'], secret_key)

        return jsonify(response)
