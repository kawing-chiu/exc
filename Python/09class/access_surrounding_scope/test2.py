from test import Test


class Test2(Test):
    def __init__(self):
        print(self.constants.THOST_FTDC_VAA_NoAvailAbility)
        print(MAX)

# works:
t = Test()
# not working:
t2 = Test2()
