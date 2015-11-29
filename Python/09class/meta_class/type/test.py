
def make_class(name, **kwargs):
    return type(name, tuple(), dict(**kwargs))

Foo = make_class('Foo', a=5, x="hehe")

foo = Foo()

class Bar:
    a = 10
    x = "good"

bar = Bar()
