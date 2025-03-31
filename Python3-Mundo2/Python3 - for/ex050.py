soma = 0
count = 0
for s in range(1,7):
    n1 = int(input('Escreva o {} numero: '.format(s)))
    if n1 % 2 == 0:
        soma += n1
        count += 1

print('Voce informou {} pares e a soma dos numeros pares é: {}'.format(count, soma))