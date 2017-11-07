from weakref import WeakSet
from functools import partial


def f(x):
    print(x)

class A:
    def __init__(self):
        self.callbacks = WeakSet()

p = partial(f, 20)

a = A()
a.callbacks.add(p)
