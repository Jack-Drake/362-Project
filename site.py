# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer # python2
from http.server import BaseHTTPRequestHandler, HTTPServer # python3
import cgi

class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            f = open("index.html", 'rb')
            self.wfile.write(f.read())
            f.close()
            return
        elif self.path == "/contact.html":
            self._set_headers()
            f = open("contact.html", 'rb')
            self.wfile.write(f.read())
            f.close()
            return
            
        
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        print(form.getvalue("name"))

host = ''
port = 80
HTTPServer((host, port), HandleRequests).serve_forever()