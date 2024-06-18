import abc

class authUsername(abc.ABC):
    @abc.abstractmethod
    def loginByUsername(self, username, password):
        pass
