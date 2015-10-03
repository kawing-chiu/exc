#include <iostream>

#include "test_class.h"

using namespace std;

void TestClass::set_attr(int i) {
    attr = i;
}

int TestClass::get_attr() {
    return attr;
}

void TestClass::call_callback() {
    TestStruct test_data = {"测试", 20};
    cout << "calling callback..." << endl;
    int ret = this->callback(&test_data);
    cout << "callback return: " << ret << endl;
}

void TestClass::set_callback(int (*callback)(TestStruct *)) {
    cout << "setting callback..." << endl;
    this->real_callback_ = callback;
}
