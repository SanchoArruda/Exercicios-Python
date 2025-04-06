import random

n_aleatorio = random.randint(0,10)

pensa = 0
count = 1
while n_aleatorio != pensa:
    pensa = int(input('Escreva um numero para advinhar: '))
    if n_aleatorio != pensa:
        count += 1
print('O numero aleatorio é {} e o jogador teve que tentar {} vezes para acertar'.format(n_aleatorio, count))
