from _built_module import ffi

lib = ffi.dlopen(None)

lib.printf(b"Hello, %d\n", ffi.cast('int', 50))
