import abc

class UserServices(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """
    @abc.abstractmethod
    def auth(self):
        pass
    @abc.abstractmethod
    def auth_user(self):
        pass
    @abc.abstractmethod
    def create_user(self):
        pass
    @abc.abstractmethod
    def read_users(self):
        pass
    @abc.abstractmethod
    def read_user(self):
        pass
    @abc.abstractmethod
    def update_user_name(self):
        pass
    @abc.abstractmethod
    def delete_user(self):
        pass

