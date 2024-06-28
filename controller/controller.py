from model.Authenticate.authManager import auth_user, register_user
from model.UserManager.userManager import get_all_users, delete_user

from service.serviceUser.ProxyUser import ProxyUser
from service.serviceUser.UserCrud import UserCrud

from service.serviceTicket.ProxyTicket import ProxyTicket
from service.serviceTicket.TicketCrud import TicketCrud

from app import app

from flask import request, jsonify, session
from werkzeug.utils import secure_filename
import os
import datetime
import base64


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
    print(result, status_code, user)
   
    if result and status_code == 200:
        print("Datos correctos")
        session["user_id"] = user['id']
        
        return jsonify({'success': result, 'message': 'Datos Correctos', 'user' : user})
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

@app.route('/remove_user/<string:id>', methods=['POST'])
def remove_user(id):
    status_code, result = delete_user(id)
    print("Valores: ", status_code, result)
    if not result:
        return jsonify({'message': 'Usuario no encontrado'}), status_code
    return jsonify({'message': 'Usuario eliminado exitosamente'}), status_code

@app.route('/change_profile_pic', methods=['POST'])
def change_profile_pic():
    try:
        id_user = request.form['id']
        profile_pic = request.files['file'].read()
        
        result, status_code = ProxyUser(UserCrud('databasetickets')).update_profile_pic(id_user, profile_pic)
        print(result, status_code)
        return jsonify({"message": "Imagen subida correctamente."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/get_profile_pic/<string:id>', methods=['POST','GET'])
def get_profile_pic(id):
    
    status_code, user = ProxyUser(UserCrud('databasetickets')).read_profile_pic(id)
    print(status_code, user['id'])
    if status_code == 200:
        return jsonify({'status_code' : 200, 'message': 'Datos Correctos', 'user' : user })
    return jsonify({'status_code' : 500, 'message' : 'error al obtener la imagen', 'user' : None})
        
#base64.b64encode(pic).decode('utf-8') if pic != None else None
@app.route('/get_tickets', methods=['GET'])
def get_tickets():
    status_code, tickets = ProxyTicket(TicketCrud('databasetickets')).get_tickets()
    print(tickets)
    if not tickets:
        return jsonify({"error": "No hay tickets"}), 401
    return jsonify(tickets)

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    print(request.json)
    year, month, day = map(int, request.json['fecha_creacion'].split('-'))
    print(year, month, day)
    new_ticket = {
        'asunto_ticket' : request.json['asunto_ticket'], 
        'descripcion_ticket' : request.json['descripcion_ticket'],
        'fecha_creacion_ticket' : request.json['fecha_creacion'],
        'categoria_ticket' : request.json['categoria_ticket'], 
        'id_usuario' : request.json['id_usuario'],
        'id_estado' : request.json['id_estado']
    }
    return ProxyTicket(TicketCrud('databasetickets')).create_ticket(new_ticket)

@app.route('/remove_ticket/<int:id>', methods=['POST'])
def remove_ticket(id):
    status_code, result = ProxyTicket(TicketCrud('databasetickets')).delete_ticket(id)
    print(status_code, result)
    if not result:
        return jsonify({'message': 'Ticket no encontrado'}), status_code
    return jsonify({'message': 'Ticket eliminado exitosamente'}), status_code

