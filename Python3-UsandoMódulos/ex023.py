#usando matemática

numero = int(input('Fale um numero de 0 a 9999: '))

n1 = numero%1000
n2 = n1%100
n3 = n2%10

milhar = int((numero-n1)/1000)
centena = int((n1-n2)/100)
dezena = int((n2-n3)/10) 

print('O numero em milhar eh: {}'.format(milhar))
print('O numero em centena eh: {}'.format(centena))
print('O numero em dezena eh: {}'.format(dezena))
print('O numero em unidade eh: {}'.format(n3))

