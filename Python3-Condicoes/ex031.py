km = int(input('Escreva a distancia em km da viagem: '))

if km <= 200:
    cobrando = 0.5 * km
    print('O valor da passagem sera de: {}'.format(cobrando))
else:
    cobrando2 = 0.45 * km
    print('O valor da passagem sera de: {}'.format(cobrando2))