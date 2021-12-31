from flask import request, jsonify
from .controller import create_user


def user_controller(server):
    @server.route('/', methods=['POST'])
    def new_user():
        username = request.json['username']
        email = request.json['email']
        response = create_user(username, email)

        return jsonify(response)
