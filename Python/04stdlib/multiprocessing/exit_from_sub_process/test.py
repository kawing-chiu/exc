from multiprocessing import Process
import sys
from time import sleep


def f():
    print('hehe')
    # no great effect, just set the exitcode:
    #sys.exit(10)

def run():
    p = Process(target=f)
    p.start()
    print("started")
    p.join()
    print(p.exitcode)
    print("joined")
    sleep(1)
    print("end")

if __name__ == '__main__':
    run()
