import collections

class OrderedClass(type):

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        print(kwds)
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result

    def __init__(cls, name, bases, namespace, **kwds):
        pass

class A(metaclass=OrderedClass, abc='kkk'):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass

a = A()
