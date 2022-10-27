from socket import socket, AF_INET, SOCK_STREAM
from email.utils import formatdate
from datetime import datetime
from time import mktime
import os

cont = 0
while True:
    socket_servidor = socket(AF_INET, SOCK_STREAM)

    socket_servidor.bind(('192.168.1.101', 8080))

    socket_servidor.listen()
    socket_cliente, endereco_cliente = socket_servidor.accept()
    dados = socket_cliente.recv(2048)
    requisicao = dados.decode()
    print('Requisição recebida: ')
    print(f'{requisicao}')

    now = datetime.now()
    stamp = mktime(now.timetuple())

    linhas = requisicao.strip().split('\r\n')

    try:
        valores_http = {}
        for i, linha in enumerate(linhas):
            if i == 0:
                colunas = linha.split(' ')
                metodo = colunas[0]
                caminho = colunas[1]
                versao_http = colunas[2]
            else:
                colunas = linha.split(':')
                valores_http[colunas[0]] = colunas[1].strip()

        if versao_http == "HTTP/1.1":

            try:
                if caminho == "/":
                    caminho_arquivo = 'C:\\Users\\Agso\\Desktop\\projetoServidorWeb\\arquivos do Servidor\\Imagem.png'

                else:
                    caminho_arquivo = caminho.replace("/","\\")
                    caminho_arquivo = caminho_arquivo.lstrip("\\")

                arquivo_requisitado = open(caminho_arquivo, 'rb')

                resposta = ''
                resposta += 'HTTP/1.1 200 OK\r\n'
                resposta += f'Date: {formatdate(timeval=stamp, localtime=False, usegmt=True)}\r\n'
                resposta += 'Server: CIn UFPE/0.0.0.0 (Windows)\r\n'
                resposta += f'Content-Length: {os.path.getsize(caminho_arquivo)}'
                resposta += 'Content-Type: application/x-unknown\r\n'
                resposta += '\r\n'

                socket_cliente.send(resposta.encode())

                while True:
                    pedaco = arquivo_requisitado.read(1024)
                    if len(pedaco) == 0:
                        break

                    socket_cliente.send(pedaco)

            except:

                resposta = ''
                resposta += 'HTTP/1.1 404 Not Found\r\n'
                resposta += f'Date: {formatdate(timeval=stamp, localtime=False, usegmt=True)}\r\n'
                resposta += '\r\n'

                html = ''
                html += '<html>'
                html += '<head>'
                html += '<title>Servidor Web</title>'
                html += '<meta charset="UTF-8">'
                html += '</head>'
                html += '<body>'
                html += '<h1>Arquivo não encontrado!</h1>'
                html += '<h2>Procure por outro arquivo...</h2>'
                html += '</body>'
                html += '</html>'

                resposta += html

                socket_cliente.send(resposta.encode())


    except:

        resposta = ''
        resposta += '400 Bad Request\r\n'
        resposta += f'Date: {formatdate(timeval=stamp, localtime=False, usegmt=True)}\r\n'
        resposta += '\r\n'

        html = ''
        html += '<html>'
        html += '<head>'
        html += '<title>Servidor Web</title>'
        html += '<meta charset="UTF-8">'
        html += '</head>'
        html += '<body>'
        html += '<h1>Mensagem de requisição não entendida pelo servidor.</h1>'
        html += '</body>'
        html += '</html>'

        resposta += html

        socket_cliente.send(resposta.encode())

socket_cliente.close()
socket_servidor.close()
