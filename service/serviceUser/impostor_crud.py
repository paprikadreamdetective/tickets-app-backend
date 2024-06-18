#from ProxyUser import ProxyUser
#from UserCrud import UserCrud
import sqlite3

# Conectar a la base de datos SQLite
def connect():
    return sqlite3.connect("sima_tickets.db")

# Crear la tabla "usuario" si no existe
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id_user TEXT PRIMARY KEY,
            tipo_usuario INTEGER,
            nombre_usuario TEXT,
            correo_usuario TEXT,
            password TEXT,
            area TEXT,
            marca TEXT,
            modelo_equipo TEXT,
            numero_serie_equipo TEXT,
            modelo_cargador TEXT,
            windows_version TEXT,
            RAM INTEGER,
            procesador TEXT,
            disco_duro TEXT,
            tipo_disco_duro TEXT,
            tarjeta_video TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Crear un nuevo usuario
def create_user(user):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuario (
            id_usuario, tipo_usuario, nombre_usuario, correo_usuario, password, area,
            marca_equipo, modelo_equipo, numero_serie_equipo, modelo_cargador,
            windows_version, RAM, procesador, disco_duro, tipo_disco_duro, tarjeta_video
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', user)
    conn.commit()
    conn.close()

# Leer usuarios
def read_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuario')
    users = cursor.fetchall()
    conn.close()
    return users

# Leer un usuario por id
def read_user(id_user):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuario WHERE id_usuario = ?', (id_user,))
    user = cursor.fetchone()
    conn.close()
    return user

# Actualizar un usuario
def update_user(user):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuario SET
            tipo_usuario = ?, nombre_usuario = ?, correo_usuario = ?, password = ?, area = ?,
            marca_equipo = ?, modelo_equipo = ?, numero_serie_equipo = ?, modelo_cargador = ?,
            windows_version = ?, RAM = ?, procesador = ?, disco_duro = ?, tipo_disco_duro = ?, tarjeta_video = ?
        WHERE id_usuario = ?
    ''', (
        user[1], user[2], user[3], user[4], user[5],
        user[6], user[7], user[8], user[9], user[10],
        user[11], user[12], user[13], user[14], user[15],
        user[0]
    ))
    conn.commit()
    conn.close()

# Eliminar un usuario
def delete_user(id_user):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuario WHERE id_user = ?', (id_user,))
    conn.commit()
    conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    #create_table()
    
    # Crear un nuevo usuario
    #user = ("1", 1, "John Doe", "john@example.com", "password123", "IT", "Dell", "Inspiron", "12345", "Dell Charger", "Windows 10", 16, "Intel i7", "512GB", "SSD", "NVIDIA GTX 1050")
    #create_user(user)
    
    # Leer todos los usuarios
    users = read_users()
    print(users)
    
    # Leer un usuario por id
    #user = read_user("1")
    #print(user)
    
    # Actualizar un usuario
    updated_user = ("1", 2, "John deSanta", "john.smith@example.com", "newpassword", "HR", "HP", "Pavilion", "67890", "HP Charger", "Windows 11", 32, "Intel i9", "1TB", "SSD", "NVIDIA RTX 2060")
    update_user(updated_user)
    
    # Eliminar un usuario
    #delete_user("1")
    
    # Leer todos los usuarios nuevamente
    users = read_users()
    print(users)
