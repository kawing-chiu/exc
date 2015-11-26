from collections import OrderedDict

from cffi import FFI

def profile(f):
    return f

ffi = FFI()

from _data_wrapper import ffi

@profile
def _struct_to_dict(data, fields, encoding):
    d = {}
    for name, field in fields:
        if field.type.kind == 'primitive':
            d[name] = getattr(data, name)
        else:
            d[name] = cdata_to_python(getattr(data, name), encoding=encoding)
    return d

@profile
def _array_to_list(data, item, length, encoding):
    if item.kind == 'primitive':
        if item.cname == 'char':
            if encoding is None:
                return ffi.string(data)
            else:
                return ffi.string(data).decode(encoding)
        else:
            return [data[i] for i in range(length)]
    else:
        return [cdata_to_python(data[i]) for i in range(length)]

@profile
def cdata_to_python(data, encoding='utf-8'):
    type_ = ffi.typeof(data)
    if type_.kind == 'primitive':
        return data
    elif type_.kind == 'pointer':
        if data == ffi.NULL:
            return None
        else:
            if isinstance(data[0], ffi.CData):
                return cdata_to_python(data[0], encoding=encoding)
            else:
                return data[0]
    elif type_.kind == 'struct':
        return _struct_to_dict(data, type_.fields, encoding=encoding)
    elif type_.kind == 'array':
        return _array_to_list(data, type_.item, type_.length, encoding=encoding)

@profile
def cdata_to_python_ver2(data, encoding='utf-8'):
    @profile
    def _struct_to_dict(data, fields):
        d = {}
        for name, field in fields:
            if field.type.kind == 'primitive':
                d[name] = getattr(data, name)
            else:
                d[name] = cdata_to_python_ver2(getattr(data, name), encoding=encoding)
        return d
    
    @profile
    def _array_to_list(data, item, length):
        if item.kind == 'primitive':
            if item.cname == 'char':
                if encoding is None:
                    return ffi.string(data)
                else:
                    return ffi.string(data).decode(encoding)
            else:
                return [data[i] for i in range(length)]
        else:
            return [cdata_to_python_ver2(data[i]) for i in range(length)]

    type_ = ffi.typeof(data)
    if type_.kind == 'primitive':
        return data
    elif type_.kind == 'pointer':
        if data == ffi.NULL:
            return None
        else:
            if isinstance(data[0], ffi.CData):
                return cdata_to_python_ver2(data[0], encoding=encoding)
            else:
                return data[0]
    elif type_.kind == 'struct':
        return _struct_to_dict(data, type_.fields)
    elif type_.kind == 'array':
        return _array_to_list(data, type_.item, type_.length)

#del profile

@profile
def cdata_to_python_ver3(data, encoding='utf-8'):
    @profile
    def _struct_to_dict(data, fields):
        d = {}
        for name, field in fields:
            if field.type.kind == 'primitive':
                d[name] = getattr(data, name)
            else:
                d[name] = _cdata_to_python_inner(getattr(data, name))
        return d
    
    @profile
    def _array_to_list(data, item, length):
        if item.kind == 'primitive':
            if item.cname == 'char':
                if encoding is None:
                    return ffi.string(data)
                else:
                    return ffi.string(data).decode(encoding)
            else:
                return [data[i] for i in range(length)]
        else:
            return [_cdata_to_python_inner(data[i]) for i in range(length)]

    @profile
    def _cdata_to_python_inner(data):
        type_ = ffi.typeof(data)
        if type_.kind == 'primitive':
            return data
        elif type_.kind == 'pointer':
            if data == ffi.NULL:
                return None
            else:
                if isinstance(data[0], ffi.CData):
                    return _cdata_to_python_inner(data[0])
                else:
                    return data[0]
        elif type_.kind == 'struct':
            return _struct_to_dict(data, type_.fields)
        elif type_.kind == 'array':
            return _array_to_list(data, type_.item, type_.length)

    return _cdata_to_python_inner(data)


@profile
def cdata_to_python_ver4(data, encoding='utf-8'):
    typeof = ffi.typeof
    @profile
    def _cdata_to_python_inner(data):
        type_ = typeof(data)
        kind = type_.kind
        if kind == 'primitive':
            return data
        elif kind == 'pointer':
            if data == ffi.NULL:
                return None
            else:
                if isinstance(data[0], ffi.CData):
                    return _cdata_to_python_inner(data[0])
                else:
                    return data[0]
        elif kind == 'struct':
            #d = {}
            d = OrderedDict()
            for name, field in type_.fields:
                kind = field.type.kind
                if kind == 'primitive':
                    d[name] = getattr(data, name)
                else:
                    d[name] = _cdata_to_python_inner(getattr(data, name))
            return d
        elif kind == 'array':
            item = type_.item
            if item.kind == 'primitive':
                if item.cname == 'char':
                    if encoding is None:
                        return ffi.string(data)
                    else:
                        return ffi.string(data).decode(encoding)
                else:
                    return [data[i] for i in range(type_.length)]
            else:
                return [_cdata_to_python_inner(data[i]) for i in range(type_.length)]

    return _cdata_to_python_inner(data)


