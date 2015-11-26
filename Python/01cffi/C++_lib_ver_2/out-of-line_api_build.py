from cffi import FFI


ffi = FFI()

ffi.set_source('_wrapper_module', '''
        #include "test_class.h"

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
    ''', libraries=['test'], source_extension='.cpp',
    # even if -ggdb3 is not specified, the resulting library is not stripped, 
    # to strip the library, '-Wl,--strip-debug' might be added, not quite sure 
    # whether it is a good approach yet
    extra_compile_args=['-std=c++11', '-Wall', '-Wextra', '-ggdb3'],
    extra_link_args=['-L.', '-Wl,-rpath,$ORIGIN', '-Wl,--no-undefined'])

ffi.cdef("""
        typedef struct TestClass TestClass;
        
        TestClass* new_test_class();
        
        void test_class_set_attr(TestClass* c, int i);
        
        int test_class_get_attr(TestClass* c);
        
        void del_test_class(TestClass* c);
    """)

def run():
    ffi.compile()

if __name__ == "__main__":
    run()
