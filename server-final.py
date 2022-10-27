from email import message
from socket import *
import json

server_port = 12606
server_socket = socket(AF_INET, SOCK_DGRAM)
print('servidor funcionando...')
server_socket.bind(("localhost", 12606))
auth = []

while True:
    client_message, client_addr = server_socket.recvfrom(2048)

    message = client_message.decode()

    obj = {}

    name = message.split('|')[0]

    password = message.split('|')[1]

    obj["name"] = name
    obj["password"] = password

    if len(auth) == 0:
        auth.append(obj)
        server_socket.sendto(f"\n {name} fez um cadastro realizado com sucesso".encode(), client_addr)
    else:
        for item in range(len(auth)):
            if auth[item].get('password') == password:
                server_socket.sendto("\nConta já existente\nTente novamente.".encode(), client_addr)
            else:
                auth.append(obj)
                server_socket.sendto(f"\n {name} fez um cadastro realizado com sucesso".encode(), client_addr)