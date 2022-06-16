import socket


socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(('example.com', 80))

connect_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(connect_items)
print(content)
socket.send(content.encode())
result = socket.recv(10024)
print(result.decode())
