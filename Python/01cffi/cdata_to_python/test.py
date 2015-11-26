from cffi import FFI
from _cffi_utils import cdata_to_python_ver4 as cdata_to_python




ffi = FFI()
ffi.cdef('''
    struct Bar {
        double d[10];
        char c[20];
    };
    struct Foo {
        int *i;
        char c[10];
        struct Bar bar;
    };
''')
foo = ffi.new('struct Foo*')
# the following is necessary:
g_i = ffi.new('int *')
foo.i = g_i
# the following is WRONG:
# foo.i = ffi.new('int *')
# foo.i is not the original object and does not have ownership
# and will point to garbage
foo.i[0] = 200
foo.c = b"hehehe"
foo.bar.d = list(range(10))

print(cdata_to_python(foo))
print(cdata_to_python(g_i))

# test for bool support
boo = ffi.new('bool *', True)
print(cdata_to_python(boo))

ffi.cdef("""
    enum THOST_TE_RESUME_TYPE
    {
            THOST_TERT_RESTART = 0,
            THOST_TERT_RESUME,
            THOST_TERT_QUICK
    };
    """)

# not sure how to work with enum yet
#enum = ffi.new('enum THOST_TE_RESUME_TYPE *', 1)
#print(ffi.string(enum))







