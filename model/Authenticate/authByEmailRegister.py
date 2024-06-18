import abc
from .Auth import Auth
from service.serviceUser.ProxyUser import ProxyUser
class authEmailRegister(Auth):
    def __init__(self, proxy: ProxyUser) -> None:
        self._proxy = proxy 
        
    def operation(self, email, password, name, lastname):
        '''
        Funcion encargada de registrar una cuenta del usuario 
        con correo electronico, contraseña, nombre, apellido
        '''
        return self._proxy.email_register(email, password, name, lastname)