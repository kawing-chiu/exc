#!/usr/bin/env bash


CXX='g++ -ggdb3 -Wall -Wextra -std=c++11 -o test -pthread'
C='gcc -ggdb3 -Wall -Wextra -std=gnu99 -o test'

if [ "$1" = python ]; then
    echo "building libtest.so and libderived.so..."
    $CXX -fPIC -shared test_class.cpp -o libtest.so
    $CXX -fPIC -shared derived_class.cpp -o libderived.so
    echo "running cffi_build.py..."
    python cffi_build.py
elif [ "$1" = C ]; then
    # the more paranoid one:
    #$CXX -shared -fPIC wrapper.cpp -L. -lderived -ltest -o libwrapper.so -Wl,--no-undefined
    echo "building libwrapper.so and main.c..."
    $CXX -shared -fPIC wrapper.cpp -L. -o libwrapper.so
    $C main.c -L. -lwrapper -lderived -ltest -Wl,-rpath,'$ORIGIN'
fi
