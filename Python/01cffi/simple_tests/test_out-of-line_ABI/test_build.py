from cffi import FFI

# this file must be included in setup.py in order for _built_module to be build 
# when the package is installed:
# setup(
#    ...
#    setup_requires=["cffi>=1.0.0"],
#    cffi_modules=["simple_example_build.py:ffi"],
#    install_requires=["cffi>=1.0.0"],
# )

ffi = FFI()
ffi.set_source('_built_module', None)
ffi.cdef("""
    int printf(const char *format, ...);
""")

ffi.compile()
