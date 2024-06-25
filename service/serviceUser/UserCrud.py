from .UserServices import UserServices

import pymysql
import bcrypt
"""
    In this script we are going to call
    the sql sentences for the db
"""
class UserCrud(UserServices):
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name
        self._connection_db = None

    def init_connection_db(self) -> None:
        self._connection_db = pymysql.connect(host='localhost', port=3309, user='root', passwd='', database=self._db_name, cursorclass=pymysql.cursors.DictCursor)

    def close_connection_db(self) -> None:
        self._connection_db.commit()
        self._connection_db.close()

    def hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
    
    def check_password(self, hashed_password, user_password) -> bool:
        return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

    def auth(self, username: str, password: str) -> bool:
        if username == 'user' and password == '123':
            return True
        else:
            return False
        
    def auth_user(self, email: str, password_input: str):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            cursor.execute("SELECT id_usuario, correo_usuario, password_usuario, rol_usuario FROM usuario WHERE correo_usuario = %s ;", (email,))
            
            user = cursor.fetchone()
            print(user)
            self.close_connection_db()
            return (True, 200, {'id' : user['id_usuario'], 'email' : user['correo_usuario'], 'role' : user['rol_usuario']}) if self.check_password(user['password_usuario'], password_input) else (False, 500)
        except Exception as e:
            self.close_connection_db()
            return str(e), 500 

    def create_user(self, user: dict):
        try:
            # Verificamos que el usuario si el usuario ya existe en la bd
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_select = "SELECT * FROM usuario WHERE id_usuario = %s"
            cursor.execute(query_select, (user['id_usuario'],))
            existing_user = cursor.fetchone()
            # Si no existe el usuario, lo insertamos en la db, si no, no realiza la insercion
            if not existing_user:
                query_insert = """
                    INSERT INTO usuario (
                        id_usuario, 
                        nombre_usuario, 
                        apellido_paterno, 
                        apellido_materno, 
                        correo_usuario, 
                        password_usuario,
                        rol_usuario, 
                        id_area, 
                        id_equipo
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(query_insert, (
                    user['id_usuario'], 
                    user['nombre_usuario'],
                    user['apellido_paterno'],
                    user['apellido_materno'], 
                    user['correo_usuario'],
                    self.hash_password(user['password_usuario']),
                    user['rol_usuario'],
                    user['id_area'],
                    user['id_equipo']
                ))
                cursor.close()
                self.close_connection_db()
                print('Usuario insertado', user)
                return 'Usuario insertado', 200
            else:
                self.close_connection_db()
                print("El usuario ya existe en la base de datos. No se ha realizado la inserción.")
                return 'El usuario ya existe en la base de datos. No se ha realizado la inserción.', 400
        except Exception as e:
            self.close_connection_db()   
            print('Error al insertar usuario', e)
            return 'Error al insertar usuario', 500
       
    def read_users(self):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_select = """
                SELECT 
                usuario.id_usuario,
                usuario.nombre_usuario,
                usuario.apellido_paterno,
                usuario.apellido_materno,
                usuario.correo_usuario,
                area.nombre_area
                FROM usuario JOIN area ON usuario.id_area = area.id_area;
            """
            cursor.execute(query_select)
            users = cursor.fetchall()
            cursor.close()
            self.close_connection_db()
            return 200, users
        except Exception as e:
            self.close_connection_db()
            return 500, str(e)
        
    def read_user(self, name_user: str):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_select = "SELECT * FROM usuario WHERE nombre_usuario = %s"
            cursor.execute(query_select, (name_user,))
            user = cursor.fetchone()
            cursor.close()
            self.close_connection_db()
            return 200, user
        except Exception as e:
            self.close_connection_db()
            return 500, str(e)

    def update_user(self, user: dict):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_update = """
                UPDATE usuario SET 
                    nombre_usuario = %s,
                    apellido_paterno = %s,
                    apellido_materno = %s,
                    correo_usuario = %s,
                    password_usuario = %s,
                    id_area = %s
                WHERE id_usuario = %s;
            """
            cursor.execute(query_update, (
                user['nombre_usuario'],
                user['apellido_paterno'],
                user['apellido_materno'],
                user['correo_usuario'],
                self.hash_password(user['password_usuario']),
                user['id_area'],
                user['id_usuario']
            ))
            cursor.close()
            self.close_connection_db()
            return 200, "Usuario actualizado exitosamente"
        except Exception as e:
            self.close_connection_db()   
            return 500, str(e)

    def update_user_name(self, user: dict):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_update = "UPDATE usuario SET nombre_usuario = %s WHERE id_usuario = %s;"
            cursor.execute(query_update, (
                user['nombre_usuario'], 
                user['id_usuario']
            ))
            cursor.close()
            self.close_connection_db()
            return 200, "Usuario actualizado exitosamente"
        except Exception as e:
            self.close_connection_db()   
            return 500, str(e)

    def delete_user(self, id_user: str):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_delete = "DELETE FROM usuario WHERE id_usuario = %s;"
            user = cursor.execute(query_delete, (id_user,))
            self.close_connection_db()
            return 200, user
        except Exception as e:
            self.close_connection_db()   
            return 500, str(e)