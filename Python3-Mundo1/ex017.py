from math import sqrt,pow

cateto_oposto = int(input('Escreva o cateto oposto: '))
cateto_adjcente = int(input('Escreva o cateto adjacente: '))

hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjcente, 2))

print('Voce digitou {} oposto e {} adjacente o resultado do hipotenusa eh: {}'.format(cateto_oposto,cateto_adjcente,hipotenusa))