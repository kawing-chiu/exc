import zmq

context = zmq.Context.instance()

socket = context.socket(zmq.PUSH)
# Bind has no queue until some one connects. So the following may block at the
# very beginning.
socket.bind("ipc://@my-pipe|jobid")
# Connect has one queue from the beginning, even if the other end has nothing
# for us to bind.
# socket.connect("ipc://@test")


