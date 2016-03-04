import time
import zmq

# simplest request-reply flow

context = zmq.Context()
socket = context.socket(zmq.REP)
# server binds while client connects
socket.bind("tcp://*:5555")

print("Current libzmq version is %s" % zmq.zmq_version())
print("Current  pyzmq version is %s" % zmq.__version__)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(0.2)

    #  Send reply back to client
    socket.send(b"World")
