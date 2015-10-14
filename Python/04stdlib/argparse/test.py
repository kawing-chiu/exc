import argparse


def _parse_args():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="")
    parser.add_argument('required_positional_arg')
    parser.add_argument('optional_positional_arg', nargs='?')

    parser.add_argument('-t', '--true-or-false', action='store_true')
    args = parser.parse_args()
    return args

def run():
    args = _parse_args()
    print(args)

if __name__ == '__main__':
    run()
