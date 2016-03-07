import sys
import time

import zmq

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

#  Do 10 requests, waiting each time for a response
for request in range(1,11):
    req = "Hello"
    if len(sys.argv) > 1:
        req += ' from ' + sys.argv[1]
    socket.send(req.encode('utf-8'))
    message = socket.recv()
    print("Received reply %s [%s]" % (request, message))
