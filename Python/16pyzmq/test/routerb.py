import zmq

PORT = 5558

context = zmq.Context()
routerb = context.socket(zmq.ROUTER)
routerb.bind('tcp://127.0.0.1:{}'.format(PORT))
