from contextlib import ExitStack


class GoodContext:
    def __init__(self, tag):
        self.tag = tag

    def __enter__(self):
        print("enter good context", self.tag)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit good context", self.tag, repr(exc_value))


class BadContext:
    def __init__(self, tag, exc_type=RuntimeError):
        self.tag = tag
        self.exc_type = exc_type

    def __enter__(self):
        print("enter bad context", self.tag)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit bad context", self.tag, repr(exc_value))
        raise self.exc_type("oops")


es = ExitStack()
es.enter_context(GoodContext('ctx1'))
es.enter_context(BadContext('ctx2'))
es.enter_context(BadContext('ctx3', ValueError))
es.enter_context(GoodContext('ctx4'))

with es:
    print('run')
