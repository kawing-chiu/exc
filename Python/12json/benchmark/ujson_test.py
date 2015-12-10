import ujson
import time
from _data import *


def run():
    begin = time.time()
    for i in range(n):
        s = ujson.dumps(data)
        d = ujson.loads(s)
    t = time.time() - begin
    print("ujson:", t, "perloop:", t / n)

if __name__ == '__main__':
    run()
