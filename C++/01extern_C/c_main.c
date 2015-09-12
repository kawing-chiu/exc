#include "c_wrapper.h"
#include <stdio.h>

int main() {
    TestClass* c = new_test_class();
    printf("In c wrapper: initial value: %i\n", test_class_get_attr(c));
    test_class_set_attr(c, 20);
    printf("In c wrapper: new value: %i\n", test_class_get_attr(c));
}
