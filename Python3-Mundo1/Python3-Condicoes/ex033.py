n1 = int(input('Escreva o primeiro numero: ')) #2
n2= int(input('Escreva o segundo numero: ')) #4
n3 = int(input('Escreva o terceiro numero: ')) #1

if n1 >= n2 and n1>= n3:
    maior = n1
elif n2 >= n1 and n2>= n3:
    maior = n2
else: 
    maior = n3

if n1 <= n2 and n1 <= n2:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else: 
    menor = n3

print("O numero {} eh o maior".format(maior))
print('O numero {} eh o menor'.format(menor))