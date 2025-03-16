frase = input('Escreva uma frase curta: ')

print('Apareceu na frase a letra a: {} vezes'.format(frase.lower().count('a')))


print('A primeira ocorrência da letra "a" está na posição {}'.format(frase.lower().find('a') + 1))
print('A última ocorrência da letra "a" está na posição {}'.format(frase.lower().rfind('a') + 1))
