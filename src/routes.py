from components.users.network import user_controller


def set_routes(server, secret_key):
    user_controller(server, secret_key)

