from model.Authenticate.authManager import auth_user, register_user
from model.UserManager.userManager import get_all_users, delete_user
from app import app

from flask import request, jsonify, session
from werkzeug.utils import secure_filename
import os

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

@app.route('/change_profile_pic', methods=['post'])
def change_profile_pic():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Guardar la información en la base de datos
        # new_image = Image(filename=filename)
        # db.session.add(new_image)
        # db.session.commit()

        return jsonify({'message': 'Image uploaded successfully', 'filename': filename}), 200