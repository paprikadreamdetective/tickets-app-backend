from config import ApplicationConfig

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_session import Session

def create_app():
    app = Flask(__name__)  # flask app object
    CORS(app, supports_credentials=True)
    app.config.from_object(ApplicationConfig)
    #Bcrypt(app)
    #Session(app)
    return app

app = create_app()  


from controller.controller import *

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)


'''
class User:
    def __init__(self):
        self._email = None
        self._password = None
        self._rol = None

    def set_email(self, email: str):
        self._email = email

    def set_password(self, password: str):
        self._password = password

    def set_rol(self, rol: str):
        self._rol = rol

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_rol(self):
        return self._rol
'''