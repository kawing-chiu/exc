

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



