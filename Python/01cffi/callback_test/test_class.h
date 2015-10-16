#ifndef __TEST_CLASS_H
#define __TEST_CLASS_H

#include "data_structs.h"

#ifdef __cplusplus

class TestClass {
    private:
        int attr = 0;
    public:
        virtual ~TestClass() {}

        void set_attr(int i);
        int get_attr();

        virtual int callback(TestStruct *data);
        virtual int callback2(int i) = 0;

        void call_callback();
        void call_callback2();

};

#else

typedef struct TestClass TestClass;

#endif

#endif
