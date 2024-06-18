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
    def username_login(self):
        pass
    @abc.abstractmethod
    def username_register(self):
        pass
    @abc.abstractmethod
    def email_login(self):
        pass
    @abc.abstractmethod
    def email_register(self):
        pass
