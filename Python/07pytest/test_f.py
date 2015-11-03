
def f(x):
    return x + 1


def test_f():
    assert f(3) == 4

def setup_function(f):
    print("setting up f...")


def test_fixture(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
