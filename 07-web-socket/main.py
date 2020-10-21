# -*- coding: utf-8 -*-
import http.server
import socketserver
import cgi
import cgitb
import os

cgitb.enable()
PORT = 8080

# Set dir
web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

# HTTP Request handler
class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        log_file = open('log.txt', 'a')

        variable = ''
        value = ''

        for key in form.keys():
            variable = str(key)
            value = str(form.getvalue(variable))
            log_file.write(variable + "\n")
            log_file.write(value + "\n")

        log_file.flush()
        self.do_GET()

        # self.do_GET()

# Create Socketserver
httpd = socketserver.TCPServer(('', PORT), HttpRequestHandler)
httpd.serve_forever()
