from socket import *

server_addr = 'localhost'
server_port = 12606
server_tuple = (server_addr, server_port)

client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("\nInsira aqui uma mensagem para o servidor:")

    client_socket.sendto(message.encode(), server_tuple)

    server_response, server_addr = client_socket.recvfrom(2048)

    print(server_response.decode())