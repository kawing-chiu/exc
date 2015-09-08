#!/usr/bin/env python2
# encoding: utf-8
"""
"""
from __future__ import print_function, division, unicode_literals
from io import open


def run():
    with open('mm') as f:
        for line in f:
            print("Read {} characters: {}"
                    .format(len(line), repr(line)))

if __name__ == "__main__":
    run()




