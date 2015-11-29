

class A(object):
    @staticmethod
    def static(x):
        print("static:", x)
        # python 3 feature:
        #print("__class__:", __class__)

    @classmethod
    def clsmethod(cls):
        print("clsmethod")

    def inst(self):
        print("instance method")


class Test(A):
    def __init__(self):
        super(Test, self).static(20)
        super(Test, self.__class__).static(20)

        super(Test, self).clsmethod()
        super(Test, self.__class__).clsmethod()

        super(Test, self).inst()


test = Test()

print("------------------")

super(Test, test).clsmethod()
super(Test, test).inst()


print("------------------")

# the one-argument-form of super is rarely used, it works like an "unbound 
# method":

# the same:
print(super(Test))
print(super(Test).__get__(None, Test))

# the same:
print(super(Test, test))
print(super(Test).__get__(test, Test))

super(Test).__get__(Test, Test).clsmethod()
super(Test).__get__(test, Test).inst()

print("------------------")

class B(A):
    # not working here:
    #parent = super(B)

    def inst(self):
        print("this is B, not A!")

# here works:
B.parent = super(B)


b = B()
print(b.parent)
b.inst()
b.parent.inst()











