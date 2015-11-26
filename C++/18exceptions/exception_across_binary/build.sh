CXX='g++ -ggdb3 -Wall -Wextra -std=c++11 -o test -pthread'
$CXX a.cpp -shared -fPIC -o liba.so -fvisibility=hidden
$CXX b.cpp -shared -fPIC -o libb.so -fvisibility=hidden
$CXX c.cpp libb.so liba.so -Wl,-rpath,'$ORIGIN'
