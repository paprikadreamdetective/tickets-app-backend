import os
from flask import request, jsonify
from app import app
#from model.authenticate.authManager import user_auth_email, user_register_email, user_auth_username,user_register_username
#from model.generateOutfit.generateOutfit import GenerateOutfit, parse_outfit_string
#from model.CaptureClothe.imageManager import sendPictureToPI
#from model.Weather.weatherManager import getCurrentWeather
#from model.CreateOutfit.gestorConjunto import create_outfit
#from model.Wardrobe.wardrobeManager import add_outfit


@app.route('/login_email', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    print("Recv data: " + str(email) + " : " + str(password))
    result, status_code = user_auth_email(email, password)
    if status_code == 200:
        print("Datos correctos")
        return jsonify({'success': 200, 'message': result}), status_code
    else:
        print("Datos incorrectos")
        return jsonify({'success': status_code, 'message': result}), status_code