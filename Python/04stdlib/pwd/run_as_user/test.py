import subprocess

from run_as_user import *


def run():

    subprocess.call(['python', './print_info.py'])

    print("------------")
    print("run as user, pwd not set:")
    run_as_user('statistician', ['python', './print_info.py'])

    print("------------")
    print("run as user, pwd set to '.':")
    run_as_user('statistician', ['python', './print_info.py'], '.')

    print("------------")
    run_as_user('statistician', ['ls'])
    run_as_user('statistician', ['ls'], '.')

if __name__ == '__main__':
    run()
