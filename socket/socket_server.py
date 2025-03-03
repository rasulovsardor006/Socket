import socket

HOST = ('127.0.0.1', 8001)  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind(HOST) 
sock.listen()  

print('I am listening your connections :)')
sent = 0 
while True:
    print('Waiting for')
    connection, address = sock.accept()  
    print(f'Connected by {address}')

    message = b'H' * 1024 * 1024 * 1024
    sent += connection.send(message[sent:]) 
    if sent >= len(message):
        break
    connection.close() 
