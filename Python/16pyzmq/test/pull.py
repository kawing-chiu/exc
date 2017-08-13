import zmq

PORT = 11111

context = zmq.Context()
puller = context.socket(zmq.PULL)
puller.bind('tcp://*:{}'.format(PORT))
