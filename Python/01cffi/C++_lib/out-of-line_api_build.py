from cffi import FFI


ffi = FFI()
ffi.set_source('_wrapper_module', '''
        #include "c_wrapper.h"
    ''', libraries=['wrapper'],
    # even if -ggdb3 is not specified, the resulting library is not stripped, 
    # to strip the library, '-Wl,--strip-all' might be added, not quite sure 
    # whether it is a good approach yet
    extra_compile_args=['-std=gnu99', '-Wall', '-Wextra', '-ggdb3'],
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
