frase = input('Escreva uma frase curta: ').lower().strip()

print('Apareceu na frase a letra a: {} vezes'.format(frase.count('a')))


print('A primeira ocorrência da letra "a" está na posição {}'.format(frase.find('a') + 1))
print('A última ocorrência da letra "a" está na posição {}'.format(frase.rfind('a') + 1))
