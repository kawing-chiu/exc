from cffi import FFI


def _struct_to_dict(data, fields):
    d = {}
    for name, field in fields:
        if field.type.kind == 'primitive':
            d[name] = getattr(data, name)
        else:
            d[name] = cdata_to_python(getattr(data, name))
    return d

def _array_to_list(data, item, length):
    if item.kind == 'primitive':
        if item.cname == 'char':
            return ffi.string(data).decode('utf-8')
        else:
            return [data[i] for i in range(length)]
    else:
        return [cdata_to_python(data[i]) for i in range(length)]


def cdata_to_python(data):
    type_ = ffi.typeof(data)
    if type_.kind == 'primitive':
        return data
    elif type_.kind == 'pointer':
        if data == ffi.NULL:
            return None
        else:
            try:
                return cdata_to_python(data[0])
            except TypeError:
                return data[0]
    elif type_.kind == 'struct':
        return _struct_to_dict(data, type_.fields)
    elif type_.kind == 'array':
        return _array_to_list(data, type_.item, type_.length)


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
#cdata_to_python(g_i)

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







