from service.serviceUser.ProxyUser import ProxyUser
from service.serviceUser.UserCrud import UserCrud
from .MasterUsers import MasterUsersManager

def delete_user(id_user: str):
    return MasterUsersManager(ProxyUser(UserCrud('databasetickets'))).delete_user(id_user)

def search_user(name_user: str):
    return MasterUsersManager(ProxyUser(UserCrud('databasetickets'))).search_user(name_user)

def update_user(user: dict):
    return MasterUsersManager(ProxyUser(UserCrud('databasetickets'))).update_user(user)

def get_all_users():
    return MasterUsersManager(ProxyUser(UserCrud('databasetickets'))).get_all_users()