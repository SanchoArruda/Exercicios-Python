import random
from time import sleep

print('-----JOGO JA VAI COMECAR----')
n1 = int(input('Escreva um numero de 0 a 5: '))

n_aleatorio = random.randint(0,5)

print('PROCESSANDO...')
sleep(2)

if n1 == n_aleatorio:
    print('Parabens voce acertou!!')
else:
    print('Poxa o numero escolhido foi: {} o computador venceu'.format(n_aleatorio))
print('---FIM---')

