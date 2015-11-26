#include "b.h"
#include <iostream>

using namespace std;


int main() {
    try {
        f();
    } catch (MyException &e) {
        cout << "catched: " << e.what() << endl;
    }
}
