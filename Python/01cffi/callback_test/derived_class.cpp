#include <iostream>

#include "derived_class.h"


using namespace std;

int DerivedClass::callback(TestStruct *data) {
    //cout << "num: " <<  data->num << endl;
    //cout << "text: " <<  data->text << endl;
    //return 5;

    TestClass::callback(data);
    return this->real_callback_(data);
}

void DerivedClass::callback2(int i) {
    this->real_callback2_(i);
}

void DerivedClass::set_callback(int (*callback)(TestStruct *)) {
    cout << "setting callback..." << endl;
    this->real_callback_ = callback;
}

void DerivedClass::set_callback2(void (*callback)(int i)) {
    cout << "setting callback2..." << endl;
    this->real_callback2_ = callback;
}







