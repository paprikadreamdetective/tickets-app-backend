from service.serviceUser.UserServices import UserServices

class SlaveSearchUser:
    def __init__(self, proxy: UserServices):
        self._proxy = proxy

    def search(self, name_user: str):
        return self._proxy.read_user(name_user)