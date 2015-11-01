#ifndef __C_WRAPPER_H
#define __C_WRAPPER_H

#include "test_class.h"

#ifdef __cplusplus
extern "C" {
#endif

//typedef struct TestClass TestClass;
//typedef struct TestStruct TestStruct;

TestClass* new_derived_class(void);

void derived_class_set_attr(TestClass* c, int i);

int derived_class_get_attr(TestClass* c);

void derived_class_set_callback(TestClass* c, int (*callback)(TestStruct *));

void derived_class_set_callback2(TestClass* c, void (*callback)(int i));

void derived_class_call_callback(TestClass* c);

void derived_class_call_callback2(TestClass* c);

void delete_derived_class(TestClass* c);

#ifdef __cplusplus
}
#endif

#endif

