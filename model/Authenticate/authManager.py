from .authByEmail import authEmail
from .authByEmailRegister import authEmailRegister
from .authAdapter import authAdapter
from service.serviceUser.ProxyUser import ProxyUser
from service.serviceUser.UserCrud import UserCrud


def user_auth_email(email: str, password: str):
    return authEmail(ProxyUser(UserCrud())).operation(email, password)

def user_register_email(email: str, password: str, name: str, lastname: str):
    return authEmailRegister(ProxyUser(UserCrud())).operation(email, password, name, lastname)

def user_auth_username(username: str, password: str):
    return authAdapter(ProxyUser(UserCrud())).loginByUsername(username, password)

def user_register_username(username: str, password: str, name: str, lastname: str):
    return authAdapter(ProxyUser(UserCrud())).registerByUsername(username, password, name, lastname)
