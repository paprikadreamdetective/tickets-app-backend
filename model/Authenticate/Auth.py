import abc 
'''
Interfaz que usaran las funcionalidades del
adapter

'''
class Auth(abc.ABC):
    @abc.abstractmethod
    def operation(self):
        pass
