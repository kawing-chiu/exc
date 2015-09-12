#include "test_class.h"
#include "c_wrapper.h"


extern "C" {
    TestClass* new_test_class(void) {
        return new TestClass();
    }

    void test_class_set_attr(TestClass* c,int i) {
        c->set_attr(i);
    }

    int test_class_get_attr(TestClass* c) {
        return c->get_attr();
    }

    void del_test_class(TestClass* c) {
        delete c;
    }


}
