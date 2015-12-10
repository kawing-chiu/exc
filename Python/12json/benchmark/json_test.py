import json
import time
from _data import *


def run():
    begin = time.time()
    for i in range(n):
        s = json.dumps(data)
        d = json.loads(s)
    t = time.time() - begin
    print("stdlib json:", t, "perloop:", t / n)

if __name__ == '__main__':
    run()

