from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is GET request. ')

    def do_POST(self):
        content_length = self.headers
        print(content_length)
#        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
#        response = BytesIO()
#        response.write(b'This is POST request. ')
#        response.write(b'Received: ')
#        response.write(body)
#        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), handler)
httpd.serve_forever()
