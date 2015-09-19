#include <iostream>

#include "test_global.h"


int main() {
    using namespace std;

    test::test_f();
    test::test_g();

    cout << "In main: " << endl;
    // not working: cannot link
    //cout << "i: " << test::i << endl;

    // works:
    cout << "j: " << test::j << endl;
}

