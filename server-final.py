from socket import *

server_port = 12606
server_socket = socket(AF_INET, SOCK_DGRAM)
print('servidor funcionando...')
server_socket.bind(("localhost", 12606))

while True:
    client_message, client_addr = server_socket.recvfrom(2048)

    print(f'\nenviado por: {client_addr} \nmensagem: {client_message}')

    server_socket.sendto("\nMnesagem recebida pelo servidor!".encode(), client_addr)