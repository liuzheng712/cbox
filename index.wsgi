import sae

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    return [start_response]

application = sae.create_wsgi_app(app)

