#ifndef __TEST_CLASS_H
#define __TEST_CLASS_H

#include "data_structs.h"

#ifdef __cplusplus

class TestClass {
    private:
        int attr = 0;
    protected:
        int (*real_callback_)(TestStruct *);
    public:
        virtual ~TestClass() {}

        void set_attr(int i);
        int get_attr();

        virtual int callback(TestStruct *data) = 0;

        void call_callback();

        void set_callback(int (*callback)(TestStruct *));
};

#else

typedef struct TestClass TestClass;

#endif

#endif
