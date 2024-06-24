from service.serviceUser.UserServices import UserServices

class SlaveUpdateUser:
    def __init__(self, proxy: UserServices):
        self._proxy = proxy

    def update(self, user: dict):
        return self._proxy.update_user(user)