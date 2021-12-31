from flask import request, jsonify
from .controller import create_user


def user_controller(server):
    @server.route('/createuser', methods=['POST'])
    def new_user():
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']

        response = create_user(username, email, password)

        return jsonify(response)
