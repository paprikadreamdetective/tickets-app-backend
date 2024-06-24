from .authAdapter import AuthAdapter
from service.serviceUser.ProxyUser import ProxyUser
from service.serviceUser.UserCrud import UserCrud

def auth_user(email: str, password: str):
    return AuthAdapter(ProxyUser(UserCrud('databasetickets'))).operation(email, password)

def register_user(user: dict):
    return AuthAdapter(ProxyUser(UserCrud('databasetickets'))).register(user)
