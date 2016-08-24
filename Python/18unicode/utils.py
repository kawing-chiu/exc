

def hex_print(s, encoding='utf-8'):
    for b in s.encode(encoding):
        print('{:0>2x}'.format(b), end=' ')

def binary_print(s, encoding='utf-8'):
    for b in s.encode(encoding):
        print('{:0>8b}'.format(b), end=' ')
