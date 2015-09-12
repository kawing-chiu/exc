#include "test_class.h"
#include <iostream>

using namespace std;

int main() {
    TestClass *c = new TestClass();
    cout << "Initial value: " << c->get_attr() << endl;
    c->set_attr(50);
    cout << "New value: " << c->get_attr() << endl;

}
