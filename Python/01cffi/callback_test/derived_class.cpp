#include <iostream>

#include "derived_class.h"


using namespace std;

int DerivedClass::callback(TestStruct *data) {
    //cout << "num: " <<  data->num << endl;
    //cout << "text: " <<  data->text << endl;
    //return 5;

    return this->real_callback_(data);
}
