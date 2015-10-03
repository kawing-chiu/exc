#include <stdio.h>

#include "wrapper.h"

int my_callback(TestStruct * data) {
    printf("text is: %s\n", data->text);
    return 50;
}

int main() {
    TestClass* c = new_derived_class();
    derived_class_set_callback(c, my_callback);
    derived_class_call_callback(c);
    delete_derived_class(c);
}
