from flask import Flask
import os
import routes

app = Flask(__name__)

SECRET_KEY = os.environ['SECRET_KEY']

routes.set_routes(app, SECRET_KEY)

if __name__ == '__main__':
    app.run(debug=True, port=3001)

