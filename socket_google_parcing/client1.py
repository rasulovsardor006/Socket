import socket
import ssl

HOST = ('www.google.com', 443)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.create_default_context()

ssl_socket = context.wrap_socket(sock, server_hostname=HOST[0])

ssl_socket.connect(HOST)

print('Connected To www.google.com')

request = b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n'
ssl_socket.sendall(request)

response = ''

while True:
    data = ssl_socket.recv(1024)
    if not data:
        break
    response += data.decode('utf-8', errors='ignore')

print(response)

response_header, _, response_body = response.partition('\r\n\r\n')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(response_body)

ssl_socket.close()
