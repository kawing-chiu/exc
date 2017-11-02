class MethodRegister(set):
    def __init__(self, *, attr):
        self.attr_name = attr

    def __call__(self, *args, **kwargs):
        def decorator(func):
            self.add(func.__name__)
            if not hasattr(func, self.attr_name):
                setattr(func, self.attr_name, [])
            attr_list = getattr(func, self.attr_name)
            attr_list.append({'args': args, 'kwargs': kwargs})
            return func
        return decorator


class _NodeMeta(type):
    @classmethod
    def __prepare__(meta, name, bases, **kwargs):
        from collections import OrderedDict
        d = OrderedDict()
        register = MethodRegister(attr='event_types')
        for cls in bases:
            if hasattr(cls, 'event_handler'):
                register.update(cls.event_handler)
                break
        d['event_handler'] = register
        return d


class A(metaclass=_NodeMeta):
    @event_handler("unpack_event", unpack_data=True)
    @event_handler("mouse_event")
    def my_method(self, arg1, arg2):
        pass

    @event_handler("key_event")
    def my_other_method():
        pass

class B(A):

    @event_handler("hehe", "abc")
    def my_method(self, x, y):
        pass

    @event_handler("good")
    def test(self, x):
        pass

b = B()

