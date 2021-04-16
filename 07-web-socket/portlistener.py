 #!/usr/bin/env python
import socket

TCP_IP = "192.168.1.5"
TCP_PORT = 8080
BUFFER_SIZE = 1024

print('Port')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
conn.close()
