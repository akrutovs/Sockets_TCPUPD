import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('127.0.0.1', 9111))

while True:
    try:
        res = socket.recv(1024)

    except KeyboardInterrupt:
        socket.close()
    else:
        print(res.decode('utf-8'))
