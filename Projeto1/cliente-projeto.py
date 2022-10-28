from lib2to3.pgen2 import token
from socket import *
import random

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False
                
        if isPrime:
            prime_list.append(n)
    return prime_list

prime_list = primesInRange(1,1000)

server_addr = 'localhost'
server_port = 12606
server_tuple = (server_addr, server_port)

client_socket = socket(AF_INET, SOCK_DGRAM)

while True:

    p = random.choice(prime_list)

    private_key_c = int(random.randint(0,100))

    public_key_c = str(p**private_key_c)

    name = input("\nInsira seu nome:" )

    password = input("\nInsira uma senha:" )

    message = name + '|' + password + '|' + str(p) + '|' + str(public_key_c)

    client_socket.sendto(message.encode(), server_tuple)

    server_response, server_addr = client_socket.recvfrom(2048)

    server_response = server_response.decode()

    server_response_public_key = int(server_response.split('.')[-1])

    server_response_q = int(server_response.split(".")[-2])

    if (server_response_public_key != 0) and (server_response_q != 0):
        client_key = server_response_public_key**private_key_c % server_response_q

    print(server_response)