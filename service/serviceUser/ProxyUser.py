from .UserServices import UserServices

class ProxyUser(UserServices):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """
    
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def auth(self, username, password):
        return self._real_subject.auth(username, password)
    
    def username_login(self, username: str, password: str):
        return self._real_subject.username_login(username, password)

    def username_register(self, username: str, password: str, name: str, lastname: str):
        return self._real_subject.username_register(username, password, name, lastname)
    
    def email_login(self, username: str, password: str):
        return self._real_subject.email_login(username, password)
    
    def email_register(self, email: str, password: str, name: str, lastname: str):
        return self._real_subject.email_register(email, password, name, lastname)
