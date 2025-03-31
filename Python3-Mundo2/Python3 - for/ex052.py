numero = int(input('Escreva um número e confira se é primo: '))

soma = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        soma += 1
if soma == 2:
    print('Esse número é primo: {}'.format(numero))
else:
    print('Esse número não é primo: {}'.format(numero))
    print('Esse numero foi divisivel {} vezes '.format(soma))    

    
   
