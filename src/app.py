from flask import Flask
import routes
from dotenv import dotenv_values

app = Flask(__name__)

ENV = dotenv_values('.env')
app.config['SECRET_KEY'] = ENV['SECRET_KEY']


routes.set_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=ENV['PORT'])
