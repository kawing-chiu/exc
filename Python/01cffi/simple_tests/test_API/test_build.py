from cffi import FFI

ffi = FFI()

ffi.set_source('_built_module',
    """
    #include <sys/types.h>
    #include <pwd.h>
    """,
    libraries=[])

ffi.cdef("""
    typedef int... uid_t;
    struct passwd {
        char *pw_name;
        uid_t pw_uid;
        ...;
    };
    struct passwd *getpwuid(int uid);
""")


ffi.compile()
