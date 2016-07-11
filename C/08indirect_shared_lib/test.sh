# from 
# http://stackoverflow.com/questions/45135/why-does-the-order-in-which-libraries-are-linked-sometimes-cause-errors-in-gcc
export LD_LIBRARY_PATH=.
g++ -fpic -shared d.cpp -o libd.so
g++ -fpic -shared b.cpp -L. -ld -o libb.so
g++ -o test -Wl,--as-needed a.cpp -L. -lb
