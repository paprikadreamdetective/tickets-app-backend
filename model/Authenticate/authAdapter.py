"""
Adapter Design Pattern

Intent: Provides a unified interface that allows objects with incompatible
interfaces to collaborate.
"""
from .Auth import Auth
from .registerUser import RegisterUser
from service.serviceUser.ProxyUser import ProxyUser

class AuthAdapter(Auth, RegisterUser):
    def __init__(self, proxy: ProxyUser) -> None:
        self._proxy = proxy
        
    def operation(self):
        print('login con email o registro con correo u operacion extra')

    def register(self, user: dict):
        return self._proxy.create_user(user)

