import test2
from test2 import test


test(50)

test2.i = 2000
test(33)

test2.i = "testing"
test(None)

del test2.i
test("no i")
