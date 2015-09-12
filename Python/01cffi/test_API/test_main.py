from _built_module import ffi, lib

p = lib.getpwuid(0)
assert ffi.string(p.pw_name) == b'root'
print(p.pw_name)
print(p.pw_uid)
