# encoding: utf-8
#from __future__ import print_function, division, unicode_literals
import shelve
import json
import time
import sys

import six

from _cffi_utils import *
from _data_wrapper import ffi, lib



def _load_shelve():
    db = shelve.open('test_shelve_2') 
    error_info = json.loads(db['error_info'])
    depth_data = json.loads(db['depth_data'])
    db.close()
    print(error_info)
    print(depth_data)
    #db = shelve.open('test_shelve') 
    #db2 = shelve.open('test_shelve_2', protocol=0) 
    #db2['error_info'] = db['error_info']
    #db2['depth_data'] = db['depth_data']
    #db.close()
    #db2.close()

    #sys.exit()
    return error_info, depth_data

def run():
    error_info, depth_data = _load_shelve()

    error_info['ErrorMsg'] = error_info['ErrorMsg'].encode('gb18030')
    error_info = ffi.new('struct CThostFtdcRspInfoField *', error_info)
    #print(cdata_to_python_ver2(error_info, encoding='gb18030'))

    for k, v in depth_data.items():
        if isinstance(v, six.text_type):
            depth_data[k] = v.encode('utf-8')
    depth_data = ffi.new('struct CThostFtdcDepthMarketDataField *', depth_data)
    #print(cdata_to_python_ver2(depth_data))

    n = 10000
    n = 1
    print(cdata_to_python_ver4(depth_data))
    sys.exit()

    #begin = time.time()
    #for i in range(n):
    #    cdata_to_python_ver4(depth_data)
    #t = time.time() - begin
    #print("depth_data, ver4: {}, {:.10f}".format(t, t/n))

    #begin = time.time()
    #for i in range(n):
    #    cdata_to_python_ver3(depth_data)
    #t = time.time() - begin
    #print("depth_data, ver3: {}, {:.10f}".format(t, t/n))

    #begin = time.time()
    #for i in range(n):
    #    cdata_to_python_ver2(depth_data)
    #t = time.time() - begin
    #print("depth_data, ver2: {}, {:.10f}".format(t, t/n))

    #begin = time.time()
    #for i in range(n):
    #    cdata_to_python(depth_data)
    #t = time.time() - begin
    #print("depth_data, ver0: {}, {:.10f}".format(t, t/n))

    begin = time.time()
    for i in range(n):
        cdata_to_python_ver4(error_info, encoding='gb18030')
    t = time.time() - begin
    print("error_info, ver4: {:.10f}".format(t/n))

    #begin = time.time()
    #for i in range(n):
    #    cdata_to_python_ver3(error_info, encoding='gb18030')
    #t = time.time() - begin
    #print("error_info, ver3: {:.10f}".format(t/n))

    #begin = time.time()
    #for i in range(n):
    #    cdata_to_python_ver2(error_info, encoding='gb18030')
    #t = time.time() - begin
    #print("error_info, ver2: {:.10f}".format(t/n))

    #begin = time.time()
    #for i in range(n):
    #    cdata_to_python(depth_data, encoding='gb18030')
    #t = time.time() - begin
    #print("error_info, ver0: {:.10f}".format(t/n))

if __name__ == '__main__':
    run()
