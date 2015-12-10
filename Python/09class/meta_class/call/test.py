from six import with_metaclass

class TestMeta(type):
    def __call__(cls, *args, **kwargs):
        print("TestMeta: __call__ cls:", cls)
        print("TestMeta: __call__ args:", args)
        print("TestMeta: __call__ kwargs:", kwargs)
        print("TestMeta: __call__ calling super().__call__", cls)
        # note that type.__call__ accepts no arguments
        # it is type's __call__ who calls __new__ of the class being defined
        call_res = super(TestMeta, cls).__call__()
        print("TestMeta: __call__ super().__call__ finished", cls)
        return call_res


class TestClass(with_metaclass(TestMeta)):
    def __new__(cls):
        print("TestClass: __new__: calling super().__new__")
        # note that __new__ is a static method, cls has to be passed manually
        new_obj = super(TestClass, cls).__new__(cls)
        print("TestClass: __new__: super().__new__ finished")
        return new_obj

    def __init__(self):
        print("TestClass: __init__")

print("Creating object")
test = TestClass(1, x="good")
print("test:", test)
