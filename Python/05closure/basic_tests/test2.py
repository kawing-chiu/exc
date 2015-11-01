

def get_closure():
    x = 500
    def test(data):
        print("x:", x)
        print("data:", data)
        print("i:", i)
    return test


test = get_closure()

# define AFTER function definition:
i = 200


def get_closure_closure(func):
    i = 2000
    return func

def get_closure_closure_closure(i):
    def get_closure_closure(func):
        return func
    return get_closure_closure

# works:
def get_closure_closure2():
    i = 3000
    def get_closure():
        x = 500
        def test(data):
            print("x:", x)
            print("data:", data)
            print("i:", i)
        return test
    return get_closure()

# not working:
@get_closure_closure
def get_closure():
    x = 500
    def test(data):
        print("x:", x)
        print("data:", data)
        print("i:", i)
    return test

@get_closure_closure_closure(5000)
def another_test():
    x = 500
    def test(data):
        print("x:", x)
        print("data:", data)
        print("i:", i)
    return test

def run():
    #1
    f = get_closure_closure(get_closure())
    f("my data")

    print("------------------")

    #2
    f = get_closure_closure2()
    f("my data2")

    print("------------------")

    #3, the same as #1
    f = get_closure()
    f("my data3")

    print("------------------")

    f = another_test()
    f("my data4")

if __name__ == '__main__':
    run()



