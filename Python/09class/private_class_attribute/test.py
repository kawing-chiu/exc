class A:
    log = '123'
    __log = '234'
    def __init__(self):
        print(self.__log)

class B(A):
    log = 'abc'
    __log = 'efg'

    def __init__(self):
        print(self.__log)
