
# Share state instead of require same identity
class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

a = Borg()
a.x = 20
b = Borg()
