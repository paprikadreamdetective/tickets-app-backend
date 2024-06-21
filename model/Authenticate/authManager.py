from .authAdapter import AuthAdapter
from service.serviceUser.ProxyUser import ProxyUser
from service.serviceUser.UserCrud import UserCrud


def auth_user(email: str, password: str):
    return AuthAdapter(ProxyUser(UserCrud('databasetickets'))).operation(email, password)

def register_user(user: dict):
    return AuthAdapter(ProxyUser(UserCrud('databasetickets'))).register(user)


if __name__ == '__main__':
    usuario = {
        'id_usuario': 'MAD-CDM-100-002',
        'nombre_usuario': 'Bob Esponja',
        'apellido_paterno': 'Pantalones',
        'apellido_materno': 'Cuadrados',
        'correo_usuario': 'bob@example.com',
        'password_usuario': 'HolaMundo',
        'rol_usuario': 'Admin',
        'id_area': 1,
        'id_equipo': 1
    }

    print(register_user(usuario))


    if auth_user('bob@example.com', 'HolaMundo'):
        print("Autorizado")
    else:
        print("No autorizado")
