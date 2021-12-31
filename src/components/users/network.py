def user_controller(server):
    @server.route('/')
    def hello():
        return 'Hello World'
