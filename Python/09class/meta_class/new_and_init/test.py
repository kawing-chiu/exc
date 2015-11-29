import six

class TestMeta(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        # note that __new__ is a static method, meta has to be passed manually
        new_cls = super(TestMeta, meta).__new__(meta, name, bases, dct)
        print("meta:", meta)
        print("bases:", bases)
        print("dict:", dct)
        return new_cls

    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        # unlike __new__, cls does not need to be passed manually
        super(TestMeta, cls).__init__(name, bases, dct)
        print("cls:", cls)
        print("bases:", bases)
        print("dict:", dct)

class TestClass(six.with_metaclass(TestMeta)):
    def f(self):
        print("in f")

    x = "hehe"

print("Creating object")
test = TestClass()
print(test.__class__.x)
