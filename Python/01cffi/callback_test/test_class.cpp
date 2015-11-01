#include <iostream>

#include "test_class.h"

using namespace std;

void TestClass::set_attr(int i) {
    attr = i;
}

int TestClass::get_attr() {
    return attr;
}

int TestClass::callback(TestStruct *data) {
    cout << "In original TestClass callback" << endl;
    return 100;
}

void TestClass::call_callback() {
    TestStruct test_data = {"测试", 20};
    cout << "calling callback..." << endl;
    int ret = this->callback(&test_data);
    cout << "callback return: " << ret << endl;
}

void TestClass::call_callback2() {
    int i = 5;
    cout << "calling callback2..." << endl;
    this->callback2(i);
}
