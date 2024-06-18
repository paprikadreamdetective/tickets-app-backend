import abc

class authUsernameRegister(abc.ABC):
    @abc.abstractmethod
    def registerByUsername(self, username, password, name, lastname):
        pass