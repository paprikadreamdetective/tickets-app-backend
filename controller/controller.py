from model.Authenticate.authManager import auth_user

import os
from flask import request, jsonify, session

from app import app


@app.route("/@me")
def get_current_session():
    user_id = session.get("user_id")
    print(user_id)
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    #user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user_id,
        "email": 'bob@example.com'
    }) 

@app.route('/login_user', methods=['POST'])
def login_user():
    result, status_code, user = auth_user(request.json['email'], request.json['password'])
    print(result, status_code)
    print(user)    
    if result and status_code == 200:
        print("Datos correctos")
        session["user_id"] = user['id']
        
        return jsonify({'success': result, 'message': 'Datos Correctos'})
    else:
        print("Datos incorrectos")
        return jsonify({'success': result, 'message': 'Datos Incorrectos'})
    
@app.route("/logout", methods=["POST"])
def logout_user():
    session.pop("name")
    return "200"