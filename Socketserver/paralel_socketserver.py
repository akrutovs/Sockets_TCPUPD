import socketserver

class ThreadingTCPServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

class EchoHandlerUDP(socketserver.BaseRequestHandler):
    def handle(self):
        data,socket = self.request
        print(f'Adress {self.client_address[0]}')
        print(f'Data {data.decode()}')
        socket.sendto (data, self.client_address)

if __name__ == '__main__':
    with ThreadingTCPServer(('0',9110),EchoHandlerUDP) as server: # you can change UDPServer to TCPserver
        server.serve_forever()