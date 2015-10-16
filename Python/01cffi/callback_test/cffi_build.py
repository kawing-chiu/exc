from cffi import FFI

ffi = FFI()

wrapper_header = open('wrapper.h', 'r').read()
wrapper_cpp = open('wrapper.cpp', 'r').read()

ffi.set_source('_wrapper_module', """
        {header}
        {cpp}
    """.format(header=wrapper_header, cpp=wrapper_cpp),
    libraries=['derived', 'test'], source_extension='.cpp',
    extra_compile_args=['-std=c++11', '-Wall', '-Wextra', '-ggdb3'],
    extra_link_args=['-L.', '-Wl,-rpath,$ORIGIN', '-Wl,--no-undefined'])

ffi.cdef("""
        typedef struct TestStruct {
            char text[20];
            double num;
        } TestStruct;

        typedef struct TestClass TestClass;

        TestClass* new_derived_class(void);
        
        void derived_class_set_attr(TestClass* c, int i);
        
        int derived_class_get_attr(TestClass* c);
        
        void derived_class_set_callback(TestClass* c, int (*callback)(TestStruct *));
        
        void derived_class_call_callback(TestClass* c);
        
        void delete_derived_class(TestClass* c);
    """)

def run():
    ffi.compile()

if __name__ == "__main__":
    run()
