from flask import Flask
import routes

app = Flask(__name__)
routes.set_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=3001)

