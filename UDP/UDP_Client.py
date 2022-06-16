import socket

#TCP
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.sendto(b'Something ', ('127.0.0.1', 9110))
#Unix
#socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
#socket.sendto(b'Something ',('unix.sock'))
