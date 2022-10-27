from socket import socket, AF_INET, SOCK_STREAM

socket_cliente = socket(AF_INET, SOCK_STREAM)

socket_cliente.connect(('localhost', 8080))

mensagem = ""
mensagem += 'GET / HTTP/1.1\r\n'
mensagem += 'Host: 192.168.1.101:8080\r\n'
mensagem += 'Connection: close\r\n'
mensagem += 'Accept-Language: pt-BR,pt;q=0.9\r\n'
mensagem += '\r\n'


socket_cliente.send(mensagem.encode())

dados = socket_cliente.recv(2048)

mensagem = dados.decode()

print('Resposta recebida: ')
print(f'{mensagem}')
