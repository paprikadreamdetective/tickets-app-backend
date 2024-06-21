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
    
    def auth_user(self, username, password):
        return self._real_subject.auth_user(username, password)
    
    def create_user(self, user):
        return self._real_subject.create_user(user)

    def read_users(self):
        return self._real_subject.read_users()
    
    def read_user(self, id_user: str):
        return self._real_subject.read_user(id_user)
    
    def update_user_name(self, update_user):
        return self._real_subject.update_user_name(update_user)
    
    def delete_user(self, id_user: str):
        return self._real_subject.delete_user(id_user)
