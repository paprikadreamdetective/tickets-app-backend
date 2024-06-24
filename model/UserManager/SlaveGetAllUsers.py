from service.serviceUser.UserServices import UserServices

class SlaveGetAllUsers:
    def __init__(self, proxy: UserServices):
        self._proxy = proxy

    def get(self):
        return self._proxy.read_users()