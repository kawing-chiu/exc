from cgi import parse_qs, escape

# http://localhost:8080/?subject=xxx

def hello_world(environ, start_response):
    print("called")
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'subject' in parameters:
        subject = escape(parameters['subject'][0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    res_body = "hello {}".format(subject)
    print("res_body:", res_body)
    return [res_body.encode('utf-8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()
