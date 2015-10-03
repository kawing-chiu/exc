#ifndef __DERIVED_CLASS_H__
#define __DERIVED_CLASS_H__

#include "test_class.h"


class DerivedClass : public TestClass {
    public:
        virtual int callback(TestStruct *data);
};


#endif
