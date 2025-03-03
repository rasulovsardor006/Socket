import socket

HOST = ('localhost', 8001)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(HOST)


while True:
    message = input('Enter your name\n')
    sock.sendall(message.encode('utf-8'))
    data = sock.recv(1024)
    print('Received', {data.decode('utf-8')})

    if message.lower == exit:
        break


