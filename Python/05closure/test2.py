

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
