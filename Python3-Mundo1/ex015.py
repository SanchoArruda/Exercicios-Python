km  = float(input('Quantos km voce andou: '))
dias = int(input('Quantos dias voce alugou: '))

valorDias = dias * 60
valorKm = km * 0.15

valortotal = valorDias + valorKm

print('Voce alugou o carro por {}dias e andou {}km, o valor que sera pago sera {} '.format(dias, km, valortotal))