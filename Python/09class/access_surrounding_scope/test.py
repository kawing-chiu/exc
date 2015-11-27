
MAX = 250

class Test:
    # not working:
    #from _data_wrapper.lib import *
    import _data_wrapper.lib as constants
    def __init__(self):
        print(self.constants.THOST_FTDC_VAA_NoAvailAbility)
        print(MAX)

def run():
    t = Test()

if __name__ == '__main__':
    run()
