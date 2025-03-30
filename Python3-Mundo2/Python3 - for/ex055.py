minha_lista = []
for peso in range(1, 6):
    peso = int(input('Escreva o seu peso: '))
    minha_lista.append(peso)

maior = minha_lista[0]
menor = minha_lista[0]

for numero in minha_lista:
    
    if numero > maior:
        print('N: {} maior que :? M: {}'.format(numero, maior))
        maior = numero

    if numero < menor:
        menor = numero

print('O maior peso é: {}'.format(maior))
print('O menor peso é: {}'.format(menor))