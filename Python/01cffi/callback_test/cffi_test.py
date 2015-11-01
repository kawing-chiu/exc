# encoding: utf-8
from __future__ import print_function, division, unicode_literals
import json

from _wrapper_module import ffi, lib



tc = lib.new_derived_class()
attr = lib.derived_class_get_attr(tc);
print("Initial value:", attr)

lib.derived_class_set_attr(tc, 50)
attr = lib.derived_class_get_attr(tc);
print("New value:", attr)

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
        return cdata_to_python(data[0])
    elif type_.kind == 'struct':
        return _struct_to_dict(data, type_.fields) 
    elif type_.kind == 'array':
        return _array_to_list(data, type_.item, type_.length)


def get_closure():
    x = 500
    def python_callback(data):
        print("testing python callback")
        #print(ffi.string(data.text))
        #print(data.num)
        data = cdata_to_python(data)
        print(data)
        print("json:", json.dumps(data))
        print("x:", x)
    
        #raise Exception

        ##pointer
        #type = ffi.typeof(data)
        #print(dir(type))
        #print(type.kind)
        #print(type.item)
        #print(dir(type.item))
    
        ## struct
        #type = ffi.typeof(data[0])
        #print(dir(type))
        ##print(type.kind)
        #for field, fieldobj in type.fields:
        #    print(field)
        #    print(fieldobj.type.kind)
    
        ## array
        #type = ffi.typeof(data[0].text)
        #print('dir type:', dir(type))
        #print('kind:', type.kind)
        #print('item:', type.item)
        #print('cname:', type.cname)
        #print('dir type.item:', dir(type.item))
        #print('item.cname:', type.item.cname)
        #print('item.kind:', type.item.kind)
        return 1000
    return python_callback

python_callback = ffi.callback('int (*callback)(TestStruct *)', error=-1)(get_closure())

lib.derived_class_set_callback(tc, python_callback)
lib.derived_class_call_callback(tc)
#try:
#    lib.derived_class_call_callback(tc)
## CANNOT catch exception, but the callback will return -1 now
#except Exception:
#    print("good")

print("-------------------")

@ffi.callback('void (*callback)(int i)')
def python_callback2(i):
    print("getting i:", i)
    raise Exception

lib.derived_class_set_callback2(tc, python_callback2)
lib.derived_class_call_callback2(tc)




