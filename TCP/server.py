import socket
import time
#это простой сервер с двумя страницами
def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #используется ip4 и TCP можно использовать
        #AF_UNIX для использования unix сокета
        server.bind(('127.0.0.1', 2000)) #подключаемся к ip и определенный порт
        server.listen(4) #слушает только 4 запроса, остальные пропускаем

        while True: #цикл для постоянного приема запросов
            client_socket, address =  server.accept() #принимаем данные
            print(client_socket,address)
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            content = load_page_from_request(data)
            client_socket.send(content)
            client_socket.send('ls /tmp'.encode('utf-8'))
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Shut down...')
def load_page_from_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\n Content-Type: text/html; charset=utf-8\r\n\r\n'
    path =  request_data.split(' ')[1]
    response = ''
    try:
        with open('views'+ path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (online_time())
        #return (HDRS_404 + "Sorry Page not found").encode('utf-8')
def online_time():
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    text = '<!DOCTYPE html>'
    text += """<html><head><title>Время</title></head><body><h1>"""
    right_now_time = time.ctime()
    text += str(right_now_time) + '</h1></body></html>"'
    response = (HDRS + text).encode('utf-8')
    return response


if __name__ == '__main__':
    start_server()