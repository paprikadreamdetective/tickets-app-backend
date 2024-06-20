import abc

class RegisterUser(abc.ABC):
    @abc.abstractmethod
    def register(self):
        pass