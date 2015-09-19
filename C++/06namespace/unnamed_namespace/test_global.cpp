#include <iostream>

#include "test_global.h"

namespace test {
    using namespace std;

    void test_f() {
        cout << "Testing" << endl;
    }

    namespace {
        int i = 50;
    }

    int j = 100;

    void test_g() {
        cout << "In test_g: " << endl;
        cout << "i: " << i << endl;
        cout << "j: " << j << endl;
    }
}

