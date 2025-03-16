from math import radians,sin,cos, tan

graus = int(input ('Escreva o grau que quer cacular: '))

radianos = radians(graus)

seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print('O numero radiano eh {}'.format(radianos))
print('O cosseno eh {:.2f} o seno eh {:.2f} e a tangente eh {:.2f}'.format(seno,cosseno,tangente))