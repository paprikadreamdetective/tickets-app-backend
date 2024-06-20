from .authUser import AuthUser
from .authAdapter import AuthAdapter
from service.serviceUser.ProxyUser import ProxyUser
from service.serviceUser.UserCrud import UserCrud


def user_auth(email: str, password: str):
    return AuthUser(ProxyUser(UserCrud())).operation(email, password)

def register_user(user: dict):
    return AuthAdapter(ProxyUser(UserCrud())).register(user)

