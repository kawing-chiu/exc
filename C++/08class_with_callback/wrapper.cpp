#include "wrapper.h"
#include "derived_class.h"

extern "C" {
    TestClass* new_derived_class(void) {
        return new DerivedClass();
    }

    void derived_class_set_attr(TestClass* c, int i) {
        c->set_attr(i);
    }

    int derived_class_get_attr(TestClass* c) {
        return c->get_attr();
    }

    void derived_class_set_callback(TestClass* c, int (*callback)(TestStruct *)) {
        c->set_callback(callback);
    }

    void derived_class_call_callback(TestClass* c) {
        c->call_callback();
    }

    void delete_derived_class(TestClass* c) {
        delete c;
    }

}
