#include <iostream>
#include <string.h>

using namespace std;


template<typename T, size_t N>
constexpr size_t size_of_array(T (&)[N]) {
    return N;
}

void f(char *str) {
    str[0] = 'c';
    cout << str << endl;
}

void g(char *strs[]) {
    cout << strs[0] << endl;
}

int main() {
    // segmentation fault:
    //f((char *)"hehe");

    // ok:
    char str[] = "hehe";
    f(str);

    char *strs[2];
    strs[0] = new char[10]();
    strcpy(strs[0], "9999");

    g(strs);
}
