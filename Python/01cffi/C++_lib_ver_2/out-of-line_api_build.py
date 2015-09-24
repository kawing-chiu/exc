from cffi import FFI


ffi = FFI()

ffi.set_source('_wrapper_module', '''
    #
