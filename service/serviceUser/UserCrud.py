import sqlite3 
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from .UserServices import UserServices
"""
    In this script we are going to call
    the sql sentences for the db

"""
class UserCrud(UserServices):
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name
        self._connection_db_users = None
    
    def init_connection_db(self) -> None:
        self._connection_db_users = sqlite3.connect(self._db_name)

    def close_connection_db(self) -> None:
        self._connection_db_users.commit()
        self._connection_db_users.close()

    def auth(self, username: str, password: str) -> bool:
        if username == 'user' and password == '123':
            return True
        else:
            return False
        
    def create_user(self, user: dict):
        try:
            # Verificamos que el usuario si el usuario ya existe en la bd
            
            #conn = self._connection_db_users
            self.init_connection_db()
            cursor = self._connection_db_users.cursor()
            query_select = "SELECT * FROM usuario WHERE id_usuario = ?"
            cursor.execute(query_select, (user['id_usuario'],))
            existing_user = cursor.fetchone()
            # Si no existe el usuario, lo insertamos en la db, si no, no realiza la insercion
            if not existing_user:
                query_insert = '''
                    INSERT INTO usuario (
                        id_usuario, tipo_usuario, nombre_usuario, correo_usuario, password, area,
                        marca_equipo, modelo_equipo, numero_serie_equipo, modelo_cargador,
                        windows_version, RAM, procesador, disco_duro, tipo_disco_duro, tarjeta_video
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                '''
                cursor.execute(query_insert, (
                    user['id_usuario'], user['tipo_usuario'], user['nombre_usuario'], user['correo_usuario'],
                    user['password'], user['area'], user['marca_equipo'], user['modelo_equipo'],
                    user['numero_serie_equipo'], user['modelo_cargador'], user['windows_version'],
                    user['RAM'], user['procesador'], user['disco_duro'], user['tipo_disco_duro'], user['tarjeta_video']
                ))
                self.close_connection_db()
                print('Usuario insertado', user)
                return 'Usuario insertado', 200
            else:
                self.close_connection_db()
                print("El usuario ya existe en la base de datos. No se ha realizado la inserción.")
                return 'El usuario ya existe en la base de datos. No se ha realizado la inserción.', 400
        except Exception as e:
            print('Error al insertar usuario', e)
            return 'Error al insertar usuario', 500

    # Leer todos los usuarios 
    def read_users(self):
        self.init_connection_db()
        cursor = self._connection_db_users.cursor()
        cursor.execute('SELECT * FROM usuario')
        users = cursor.fetchall()
        self.close_connection_db()
        return users
    
    # Leer un usuario por id
    def read_user(self, id_user: str):
        self.init_connection_db()
        cursor = self._connection_db_users.cursor()
        cursor.execute('SELECT * FROM usuario WHERE id_usuario = ?', (id_user,))
        user = cursor.fetchone()
        self.close_connection_db()
        return user

    # Actualizar un usuario
    def update_user(self, user: dict):
        self.init_connection_db()
        cursor = self._connection_db_users.cursor()
        cursor.execute('''
            UPDATE usuario SET
                tipo_usuario = ?, nombre_usuario = ?, correo_usuario = ?, password = ?, area = ?,
                marca_equipo = ?, modelo_equipo = ?, numero_serie_equipo = ?, modelo_cargador = ?,
                windows_version = ?, RAM = ?, procesador = ?, disco_duro = ?, tipo_disco_duro = ?, tarjeta_video = ?
            WHERE id_usuario = ?
        ''', (
            user['id_usuario'], user['tipo_usuario'], user['nombre_usuario'], user['correo_usuario'],
            user['password'], user['area'], user['marca_equipo'], user['modelo_equipo'],
            user['numero_serie_equipo'], user['modelo_cargador'], user['windows_version'],
            user['RAM'], user['procesador'], user['disco_duro'], user['tipo_disco_duro'], user['tarjeta_video']
        ))
        self.close_connection_db()

    # Eliminar un usuario
    def delete_user(self, id_user: str):
        self.init_connection_db()
        cursor = self._connection_db_users.cursor()
        cursor.execute('DELETE FROM usuario WHERE id_usuario = ?', (id_user,))
        self.close_connection_db()   