import sys

import zmq

from o32.utils import patch_socket

patch_socket()

if len(sys.argv) == 2:
    id_ = sys.argv[1].encode()
else:
    id_ = None

PORT = 11111

context = zmq.Context()
dealerc = context.socket(zmq.DEALER, send_timeout=1000)
dealerc.immediate = 1
if id_ is not None:
    dealerc.identity = id_
dealerc.connect('tcp://10.38.31.23:{}'.format(PORT))


