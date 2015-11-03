import pytest

def f():
    raise SystemExit(1)

def test_f():
    with pytest.raises(SystemExit):
        f()
