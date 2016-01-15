#!/usr/bin/env python
from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# disable default keymaps
for key in mpl.rcParams:
    if key.startswith('keymap'):
        print(key, mpl.rcParams[key])
        mpl.rcParams[key] = ''

input_ = ''

def press(event):
    global input_

    key = event.key
    #print(key)

    if key.isdigit():
        input_ += key
    elif key == 'backspace':
        #input_ = input_[:-1]
        input_ = ''

    xl = ax.set_xlabel(input_)
    fig.canvas.draw()

    if len(input_) >= 6:
        print("got: {}".format(input_))
        input_ = ''

    if event.key == '\n':
        sys.stdout.write('\n')
    sys.stdout.flush()

fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')

plt.show()
