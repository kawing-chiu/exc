class MethodRegister(set):
    def __init__(self, *, attr, opt_args=True):
        self.attr_name = attr
        self.opt_args = opt_args

    def _tag_func(self, func, args, kwargs):
        self.add(func.__name__)
        if not hasattr(func, self.attr_name):
            setattr(func, self.attr_name, [])
        tag_list = getattr(func, self.attr_name)
        tag_list.append({'args': args, 'kwargs': kwargs})
        return func

    def __call__(self, *args, **kwargs):
        if (self.opt_args and len(args) == 1 and
                callable(args[0]) and not kwargs):
            # Without decorator argument, use the function name as argument
            func = args[0]
            return self._tag_func(func, (func.__name__,), kwargs)
        else:
            def decorator(func):
                return self._tag_func(func, args, kwargs)
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
        """Original doc."""
        pass

    @event_handler("key_event")
    def my_other_method():
        pass

class B(A):

    @event_handler("hehe", "abc")
    @event_handler
    def my_method(self, x, y):
        """Original doc 2."""
        pass

    @event_handler("good")
    def test(self, x):
        pass

b = B()

