import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server…")
socket.connect("tcp://localhost:5556")

# XXX: note that the client will lose the first messages the server sent 
# because of the connecting cost

zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

# Python 2 - ascii bytes to unicode str
if isinstance(zip_filter, bytes):
    zip_filter = zip_filter.decode('ascii')
#socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
socket.setsockopt_string(zmq.SUBSCRIBE, "10001")
socket.setsockopt_string(zmq.SUBSCRIBE, "10003")

total_temp = 0
for update_nbr in range(5):
    string = socket.recv_string()
    print(string)
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

print("Average temperature for zipcode '%s' was %dF" % (
      zip_filter, total_temp / update_nbr)
)
