from flask import Flask
import routes
from dotenv import dotenv_values

app = Flask(__name__)

ENV = dotenv_values('.env')

app.config.from_object('config.DevConfig')

routes.set_routes(app)

if __name__ == '__main__':
    app.run()
