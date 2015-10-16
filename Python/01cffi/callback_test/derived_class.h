#ifndef __DERIVED_CLASS_H__
#define __DERIVED_CLASS_H__

#include <string>
#include <map>

#include "test_class.h"


class DerivedClass : public TestClass {
    public:
        virtual int callback(TestStruct *data);
        virtual int callback2(int i);
        void set_callback(int (*callback)(TestStruct *));
        void set_callback2(int (*callback)(int i));

        //template<typename Func>
        //void set_callback(std::string name, Func f) {
        //    if (name == "callback1") {
        //        real_callback_ = f;
        //    } else if (name == "callback2") {
        //        real_callback2_ = f;
        //    }
        //}
    private:
        int (*real_callback_)(TestStruct *);
        int (*real_callback2_)(int i);
};


#endif
