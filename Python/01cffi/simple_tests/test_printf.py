from cffi import FFI

# simplest inline ABI version
ffi = FFI()

ffi.cdef("""
    int printf(const char *format, ...);
""")
clib = ffi.dlopen(None)
word = ffi.new('char[]', b"world")
clib.printf(b"hello, %s\n", word)

