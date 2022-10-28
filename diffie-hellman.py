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

#client calcula o p
p = random.choice(prime_list)

#server calcula o q
q = random.choice(prime_list)

#client envia o p

#server responde com o q


#client define sua chave privada
private_key1 = int(random.randint(0,1000))

#server define sua chave privada
private_key2 = int(random.randint(0,1000))


#Client usa seu p e o q enviado por server pra calcular chave pública
public_key1 = p**private_key1 % q

#Server usa seu q e o p enviado por client pra calcular chave pública
public_key2 = p**private_key2 % q

#Client calcula chave de criptografia
client1 = public_key2**private_key1 % q

#Server calcula chave de criptografia igual
client2 = public_key1**private_key2 % q

print(client1)
print(client2)
