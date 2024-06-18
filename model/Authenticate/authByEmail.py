import abc
from .Auth import Auth
from service.serviceUser.ProxyUser import ProxyUser
class authEmail(Auth):
    def __init__(self, proxy: ProxyUser) -> None:
        self._proxy = proxy 
    
    def operation(self, email, password):
        '''
        Metodo encargado de autentitifcar la cuenta del usuario 
        con correo electronico y contraseña
        '''
        return self._proxy.email_login(email, password)

    