"""
Adapter Design Pattern

Intent: Provides a unified interface that allows objects with incompatible
interfaces to collaborate.
"""

from .Auth import Auth
from .authByUsername import authUsername
from .authByUsernameRegister import authUsernameRegister
from service.serviceUser.ProxyUser import ProxyUser

class authAdapter(Auth, authUsername, authUsernameRegister):
    def __init__(self, proxy: ProxyUser) -> None:
        self._proxy = proxy
        
    def operation(self):
        print('login con email o registro con correo u operacion extra')

    def loginByUsername(self, username, password):
        return self._proxy.username_login(username, password)

    def registerByUsername(self, username, password, name, lastname):
        return self._proxy.username_register(username, password, name, lastname)
