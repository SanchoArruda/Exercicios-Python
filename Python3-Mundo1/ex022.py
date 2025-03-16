v1 = str(input('Escreva o nome completo seu: '))

print('Com letra maiuscula: ',v1.upper())
print('Com letra minuscula: ',v1.lower())
print('Quantidade de caracteres (sem espaços):', len(v1.replace(" ", "")))
primeiro_nome = v1.split()[0]
print('Quantidade de letras no primeiro nome:', len(primeiro_nome))

