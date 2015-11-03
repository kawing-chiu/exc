
class TestCls:
    # __init__() should not be defined:
    #def __init__(self):
    #    pass

    def test_1(self):
        x = "this"
        assert 'h' in x

    def test_2(self):
        print("in test_2")
        assert 1

    def not_run(self):
        print("not_run running")
