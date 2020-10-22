# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import cgi
import cgitb
import os

cgitb.enable()

PORT = 8080
blindStorage = []

# Set dir
web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

class Blind:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def getId(self):
        return self.id

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

class WebSocket:
    def __init__(self, port = 8080):
        self.port = port
        httpd = socketserver.TCPServer(('', self.port), HttpRequestHandler)
        httpd.serve_forever()

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

        # Add Log file
        log_file = open('log.txt', 'a')

        blindCreateStatus = True
        for i, item in enumerate(blindStorage):
            if item.getId() == form.getvalue('id'):
                blindStorage[i].setStatus(form.getvalue('blind'))
                blindCreateStatus = False
                log_file.write('UPDATE: ' + form.getvalue('id') + ' => ' + form.getvalue('blind') + '\n')

        if blindCreateStatus == True:
            blindStorage.append(Blind(form.getvalue('id'), form.getvalue('blind')))
            log_file.write('CREATE: ' + form.getvalue('id') + ' => ' + form.getvalue('blind') + '\n')

        log_file.flush()
        self.do_GET()

webSocketThread = threading.Thread(target=WebSocket)
webSocketThread.start()
