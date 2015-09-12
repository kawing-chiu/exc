from _wrapper_module import ffi, lib


tc = lib.new_test_class()
attr = lib.test_class_get_attr(tc);
print("Initial value:", attr)
lib.test_class_set_attr(tc, 50)
attr = lib.test_class_get_attr(tc);
print("New value:", attr)
