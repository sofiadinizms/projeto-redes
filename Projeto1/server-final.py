from email import message
from socket import *
import random

server_port = 12606
server_socket = socket(AF_INET, SOCK_DGRAM)
print('servidor funcionando...')
server_socket.bind(("localhost", 12606))
auth = []


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

prime_list = primesInRange(1,100)

while True:

    client_message, client_addr = server_socket.recvfrom(2048)

    q = random.choice(prime_list)

    private_key_s = int(random.randint(0,1000))

    message = client_message.decode()

    obj = {}

    name = message.split('|')[0]

    password = message.split('|')[1]

    p = int(message.split('|')[2])

    public_key_c = int(message.split('|')[3])

    public_key_s =  p**private_key_s % q

    diffie_key = public_key_c**private_key_s % q

    
    obj["diffie_key"] = diffie_key
    obj["name"] = name
    obj["password"] = password


    if len(auth) == 0:
        auth.append(obj)
        server_socket.sendto(f"\n {name} fez um cadastro realizado com sucesso. {q}.{public_key_s}".encode(), client_addr)
        print(auth)
    else:
        for item in range(len(auth)):
            if auth[item].get('password') == password:
                server_socket.sendto("\n Senha já existente, tente novamente.0.0".encode(), client_addr)
            else:
                auth.append(obj)
                server_socket.sendto(f"\n {name} fez um cadastro realizado com sucesso.{q}.{public_key_s}".encode(), client_addr)
                print(auth)
                