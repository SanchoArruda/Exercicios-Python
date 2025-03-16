velocidade = int(input('Escreva a velocidade que esta: '))

if velocidade > 80:
    print('Voce foi multado')
    multa = velocidade-80
    pagar = multa*7
    print('O valor que vai ter que pagar eh de: {} reais'.format(pagar))
else:
    print('Parabens voce eh um menino bom!!')