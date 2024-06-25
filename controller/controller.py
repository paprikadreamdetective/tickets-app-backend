from model.Authenticate.authManager import auth_user
from model.Authenticate.authManager import register_user
from model.UserManager.userManager import get_all_users
from app import app

from flask import request, jsonify, session



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

@app.route("/get_users", methods=["GET"])
def get_users():
    status_code, users = get_all_users()
    #print(users)
    if not users:
        return jsonify({"error": "No hay usuarios"}), 401
    return jsonify(users)

@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = {
        'id_usuario' : request.json['id_usuario'], 
        'nombre_usuario' : request.json['nombre_usuario'],
        'apellido_paterno' : request.json['apellido_paterno'],
        'apellido_materno' : request.json['apellido_materno'], 
        'correo_usuario' : request.json['correo_usuario'],
        'password_usuario' : request.json['password_usuario'],
        'rol_usuario' : request.json['rol_usuario'],
        'id_area' : request.json['id_area'],
        'id_equipo' : 1
    }
    return register_user(new_user)