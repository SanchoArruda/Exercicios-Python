v1 = str(input('Escreva o nome completo seu: '))

print('Com letra maiuscula: {}'.format(v1.upper()))
print('Com letra minuscula: {}'.format(v1.lower()))
print('Quantidade de caracteres (sem espaços): {}'.format(len(v1.replace(" ", ""))))

primeiro_nome = v1.split()
print('Seu primeiro nome eh: {} e ele tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))
