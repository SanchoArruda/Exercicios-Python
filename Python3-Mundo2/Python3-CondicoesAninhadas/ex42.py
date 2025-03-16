r1 = int(input('Escreva o comprimeiro do primeiro lado: '))
r2 = int(input('Escreva o comprimeiro do segundo lado: '))
r3 = int(input('Escreva o comprimeiro do terceiro lado: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('TRUE - os lados formam um triangulo')
    if r1 % r2 == 0 and r1 % r3 == 0 and r2 % r3 == 0:
        print('Todos os lados iguais portanto é um EQUILÁTERO')
    elif (r1 % r2 == 0 and r1 % r3 != 0) or (r1 % r2 != 0 and r1 % r3 == 0):
        print('Pelo menos 2 lados igauis portanto é um ISÓSCELES')
    else:
        print('Todos os lados são diferentes portanto é um ESCALENO')
else:
    print('false - nao forma um triangulo')
