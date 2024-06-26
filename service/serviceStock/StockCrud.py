from .StockServices import StockServices

import pymysql
"""
    In this script we are going to call
    the sql sentences for the db
"""
class StockCrud(StockServices):
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name
        self._connection_db = None

    def init_connection_db(self) -> None:
        self._connection_db = pymysql.connect(host='localhost', port=3309, user='root', passwd='', database=self._db_name, cursorclass=pymysql.cursors.DictCursor)

    def close_connection_db(self) -> None:
        self._connection_db.commit()
        self._connection_db.close()
    '''
    def create_product(self, product: dict):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_select = "SELECT * FROM  WHERE id_usuario = %s"
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
    '''