import zmq


PORT = 11111

context = zmq.Context()
dealerb = context.socket(zmq.DEALER)
dealerb.immediate = 1
dealerb.bind('tcp://*:{}'.format(PORT))

