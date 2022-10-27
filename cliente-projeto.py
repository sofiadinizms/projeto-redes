from socket import *
from random import randint

server_addr = 'localhost'
server_port = 12606
server_tuple = (server_addr, server_port)

client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    name = input("\nInsira seu nome:" )

    password = input("\nInsira uma senha:" )

    message = name + '|' + password

    client_socket.sendto(message.encode(), server_tuple)

    server_response, server_addr = client_socket.recvfrom(2048)

    print(server_response.decode())