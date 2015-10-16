#include <iostream>

#include "derived_class.h"

using namespace std;

int callback1(TestStruct *) {
    cout << "Got callback1" << endl;
    return 0;
}

int callback2(int i) {
    cout << "Got callback2" << endl;
    return i + 50;
}

int main() {
    DerivedClass d{};
    d.set_callback(callback1);
    d.set_callback2(callback2);
    d.call_callback();
    d.call_callback2();
}
