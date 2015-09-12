#ifndef __C_WRAPPER_H
#define __C_WRAPPER_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct TestClass TestClass;

TestClass* new_test_class(void);

void test_class_set_attr(TestClass* c, int i);

int test_class_get_attr(TestClass* c);

void del_test_class(TestClass* c);

#ifdef __cplusplus
}
#endif

#endif
