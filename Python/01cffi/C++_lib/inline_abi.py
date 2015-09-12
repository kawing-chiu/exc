from cffi import FFI


ffi = FFI()
ffi.cdef("""
    typedef struct TestClass TestClass;
    
    TestClass* new_test_class();
    
    void test_class_set_attr(TestClass* c, int i);
    
    int test_class_get_attr(TestClass* c);
    
    void del_test_class(TestClass* c);
""")
lib = ffi.dlopen('./libwrapper.so')

tc = lib.new_test_class()
attr = lib.test_class_get_attr(tc);
print("Initial value:", attr)
lib.test_class_set_attr(tc, 50)
attr = lib.test_class_get_attr(tc);
print("New value:", attr)



