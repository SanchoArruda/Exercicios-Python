numero = int(input('Escreva um numero qualquer: '))
base = int(input('Escreva a base de conversao: (1)binario,(2)octal, (3)hexadecimal: '))

if base == 1:
    print('O numero convertido em binario eh: {}'.format(bin(numero)))
elif base == 2:
    print('O numero convertido em octal eh: {}'.format(oct(numero)))
elif base == 3:
    print('O numero convertido em hexadecimal eh: {}'.format(hex(numero)))
else:
    print('Nenhum numero foi digitado.')
