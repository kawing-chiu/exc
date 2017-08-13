import functools

import zmq


class Socket(zmq.Socket):
    def __init__(self, *args, default_timeout=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__['_default_timeout'] = default_timeout

    def on_timeout(self):
        raise zmq.Again

    def _send_wrapper(f):
        def wrapper(self, *args, **kwargs):
            timeout = kwargs.pop('timeout', self._default_timeout)
            print("timeout:", timeout)
            ret = self.poll(timeout, zmq.POLLOUT)
            if ret:
                return f(self, *args, **kwargs)
            else:
                return self.on_timeout()
        return functools.update_wrapper(wrapper, f, ('__name__', '__doc__'))

    for _meth in dir(zmq.Socket):
        if _meth.startswith('send'):
            locals()[_meth] = _send_wrapper(getattr(zmq.Socket, _meth))

    del _meth, _send_wrapper

def patch_socket():
    zmq.Context._socket_class = Socket

def create_socket(context, type, connect_type, endpoint,
        identity=None, random_port=False):
    if connect_type not in ['bind', 'connect']:
        msg = "Invalid 'connect_type' argument"
        raise ValueError(msg)
    sock = context.socket(type)
    sock.setsockopt(zmq.IMMEDIATE, 1)
    if identity is not None:
        sock.identity = identity
    if not random_port:
        if connect_type == 'bind':
            sock.bind(endpoint)
        elif connect_type == 'connect':
            sock.connect(endpoint)
        return sock
    else:
        if connect_type == 'bind':
            port = sock.bind_to_random_port(endpoint)
        elif connect_type == 'connect':
            msg = "Cannot connect to a random port"
            raise ValueError(msg)
        return sock, port
