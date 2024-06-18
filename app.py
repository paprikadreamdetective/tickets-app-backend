from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)  # flask app object
    CORS(app)
    return app

app = create_app()  # Creating the app
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from controller.controller import *

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)