import zmq

PORT = 11111

context = zmq.Context()
pusher = context.socket(zmq.PUSH)
#pusher.setsockopt(zmq.IMMEDIATE, 1)
pusher.connect('tcp://127.0.0.1:{}'.format(PORT))

