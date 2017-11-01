class Registry(dict):
    def __call__(self, *args):
        def decorator(func):
            self[func] = args
            return func
        return decorator

class MyClass:
    register = Registry()

    @register("tag1", "tag2")
    def my_method(arg1, arg2):
        pass

    @register("tag3")
    def my_other_method(arg1, arg2):
        pass
