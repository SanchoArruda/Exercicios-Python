soma = 0

for s in range(1,6):
    n1 = int(input('Escreva o {} numero: '.format(s)))
    if n1 % 2 == 0:
        soma += n1

print('A soma dos numeros é: {}'.format(soma))