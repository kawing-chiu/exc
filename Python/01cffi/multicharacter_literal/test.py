from cffi import FFI

ffi = FFI()

ffi.set_source('_test_module', """
#define A '102001'
#define B '102001'
#define C '102001'
""", extra_compile_args=['-std=gnu99', '-Wall', '-Wextra', '-ggdb3'])

ffi.cdef("""
static const int A;
static const long B;
static const char C;
""")

ffi.compile()

from _test_module import lib
print(lib.A, lib.B, lib.C)
print(ord(lib.C))

