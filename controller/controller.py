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
import pymysql
import datetime
import base64
import pymysql

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
    result, message, status_code = register_user(new_user)
    if result and status_code == 200:
        return jsonify({'success' : result, 'message' : message})
    elif not result and status_code == 500:
        return jsonify({'success' : result, 'message' : message})
    else:
        return jsonify({'success' : result, 'message' : message})

@app.route('/remove_user/<string:id>', methods=['POST'])
def remove_user(id):
    status_code, result = delete_user(id)
    print("Valores: ", status_code, result)
    if result and status_code == 200:
        return jsonify({'success' : result, 'message': 'Usuario eliminado exitosamente'})
    elif not result and status_code == 200:
        return jsonify({'success' : result, 'message': 'Usuario no encontrado'})
    else:
        return jsonify({'success' : False, 'message': result})

@app.route('/edit_user', methods=['POST', 'GET'])
def edit_user():
    update_user = {
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
    result, message, status_code = ProxyUser(UserCrud('databasetickets')).update_user(update_user)
    print(result, message, status_code)
    if result and status_code == 200:
        return jsonify({'success' : True, 'message' : message})
    else: 
        return jsonify({'success' : False, 'message' : message})

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

'''
A partir de este punto se dejaron de usar
patrones de diseño 03/07/2024

'''

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='databasetickets',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/get_messages', methods=['GET'])
def get_messages():
    sender_id = request.args.get('sender_id')
    receiver_id = request.args.get('receiver_id')
    
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "SELECT * FROM messages WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s) ORDER BY timestamp"
        cursor.execute(sql, (sender_id, receiver_id, receiver_id, sender_id))
        messages = cursor.fetchall()
        for message in messages:
            message['timestamp'] = message['timestamp'].isoformat()
    
        conn.close()
    return jsonify(messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    sender_id = request.json['sender_id']
    receiver_id = request.json['receiver_id']
    message = request.json['msg']
    
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "INSERT INTO messages (sender_id, receiver_id, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (sender_id, receiver_id, message))
        conn.commit()
    
    conn.close()
    return jsonify({"status": "Message sent"})

@app.route('/get_areas', methods=['GET'])
def get_areas():
    #sender_id = request.args.get('sender_id')
    #receiver_id = request.args.get('receiver_id')
    
    conn = get_db_connection()
    with conn.cursor() as cursor:
        # sql = "SELECT * FROM messages WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s) ORDER BY timestamp"
        sql_query = """
            SELECT * FROM area ; 
        """
        cursor.execute(sql_query)
        areas = cursor.fetchall()
        for area in areas:
            print(area)
        
    
        conn.close()
    return jsonify(areas)

# obtener empleados por area:
@app.route('/get_area_users', methods=['GET'])
def get_area_users():
    #sender_id = request.args.get('sender_id')
    #receiver_id = request.args.get('receiver_id')
    area = request.args.get('area')
    conn = get_db_connection()
    with conn.cursor() as cursor:
        # sql = "SELECT * FROM messages WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s) ORDER BY timestamp"
        sql_query = """
            SELECT * FROM usuario JOIN area ON usuario.id_area = area.id_area WHERE area.id_area = %s ; 
        """
        cursor.execute(sql_query, (area))
        users_per_area = cursor.fetchall()
        for user in users_per_area:
            print(user)
        
    
        conn.close()
    return jsonify(users_per_area)

