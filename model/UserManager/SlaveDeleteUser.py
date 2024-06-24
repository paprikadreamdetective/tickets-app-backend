from service.serviceUser.UserServices import UserServices

class SlaveDeleteUser:
    def __init__(self, proxy: UserServices):
        self._proxy = proxy

    def delete(self, id_user: str):
        return self._proxy.delete_user(id_user)