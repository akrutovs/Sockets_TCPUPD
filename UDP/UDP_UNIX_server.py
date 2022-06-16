import socket
import os
#use unix file to transfer a information
socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

unix_sock_name = 'unix.sock'

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

socket.bind(unix_sock_name)

while True:
    try:
        res = socket.recv(1024)

    except KeyboardInterrupt:
        socket.close()
    else:
        print(res.decode('utf-8'))
