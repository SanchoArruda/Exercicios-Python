

n1 = int(input('Escreva o fatorial de: '))

n2 = 0
fatorial = 1
fatores = ''
while n2 < n1:
    n2 += 1
    fatorial *= n2
    fatores += '{} * '.format(n2)

fatores = fatores.rstrip(' *') #removendo o ultimo *

print('{}! = {} = {}'.format(n1, fatores, fatorial))
    
