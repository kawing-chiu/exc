import time
import zmq
from random import randrange, choice

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    zipcode = randrange(10000, 10100)
    #zipcode = choice([])
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    str_ = "%i %i %i" % (zipcode, temperature, relhumidity)
    #if zipcode == 10001:
    #    print("sending " + str_)
    socket.send_string(str_)
    time.sleep(0.02)
