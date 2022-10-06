# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer # python2
from http.server import BaseHTTPRequestHandler, HTTPServer # python3
import cgi
import os
import smtplib
import json
import io

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD =os.environ.get('EMAIL_PASS')



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
        elif self.path == "/logo.png":
            self._set_headers()
            f = open("logo.png", 'rb')
            self.wfile.write(f.read())
            f.close()
            return
            
        
    def do_POST(self):
        if self.path == "/contact":
            #handle form
            self._set_headers()
            form = cgi.FieldStorage(
                fp = self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            print(form.getvalue("name"))

            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                self.subject = form.getvalue("name")
                self.body = form.getvalue("message")
                self.email = form.getvalue("email")
                
                msg = f'Subject: {self.subject}\n\n{self.body}'
                smtp.sendmail(EMAIL_ADDRESS, self.email, msg)
        elif self.path == "/requestRandomRecipe":
            #send  random request
            print("here")
            self.wfile.write(io.BytesIO("123"))
        

host = ''
port = 1234
HTTPServer((host, port), HandleRequests).serve_forever()