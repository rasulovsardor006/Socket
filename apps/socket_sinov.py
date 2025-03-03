from os import write
import socket
from sqlite3 import connect
from ssl import SOL_SOCKET
import select

HOST = ('localhost', 8001)
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sock_server.bind(HOST)
sock_server.listen()
socket_server = [sock_server]
print("I'm listinging your connections")

while True:
    print('Wait for')
    readable, _, exception = select.select(socket_server, [], [])
    print(readable)
    for connection in readable:
        if connection == sock_server:
            client, address = sock_server.accept()
            print(f"New connection from {address}")
            socket_server.append(client)
        else:
            data = connection.recv(1024).decode('utf-8') 
            if not data:
                print(f"Connection closed by {address}")
                socket_server.remove(connection)
                connection.close()
            else:
                for client in socket_server:
                    if client != sock_server and client != connection:
                        client.send(f'server message: {data}'.encode('utf-8'))
                        








