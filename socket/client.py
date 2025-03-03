import socket

HOST = ('127.0.0.1', 8001)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(HOST)

print('Connected To socket', HOST)

response = ''

while True:
    data = sock.recv(1024 *1024 * 1024)
    if not data:
        break
    response += data.decode('utf-8')
print(len(response))





