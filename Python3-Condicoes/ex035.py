r1 = int(input('Escreva o comprimeiro do primeiro lado: '))
r2 = int(input('Escreva o comprimeiro do segundo lado: '))
r3 = int(input('Escreva o comprimeiro do terceiro lado: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('TRUE - os lados formam um triangulo')
else:
    print('false - nao forma um triangulo')
