from .SlaveDeleteUser import SlaveDeleteUser
from .SlaveSearchUser import SlaveSearchUser
from .SlaveUpdateUser import SlaveUpdateUser
from .SlaveGetAllUsers import SlaveGetAllUsers
from service.serviceUser.UserServices import UserServices

class MasterUsersManager:
    def __init__(self, proxy: UserServices) -> None:
        self._proxy = proxy

    def delete_user(self, id_user: str):
        return SlaveDeleteUser(self._proxy).delete(id_user)
    
    def search_user(self, name_user: str):
        return SlaveSearchUser(self._proxy).search(name_user)
    
    def update_user(self, user: dict):
        return SlaveUpdateUser(self._proxy).update(user)
    
    def get_all_users(self, user: dict):
        return SlaveGetAllUsers(self._proxy).get()