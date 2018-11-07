import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")

while True:
    msg = socket.recv()
    msg = msg.decode('utf-8')
    print("Received request: %s" % msg)
    socket.send(b"World")
