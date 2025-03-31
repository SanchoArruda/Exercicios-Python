n1 = int(input('Escreva o numero que deseja saber a tabuada: '))

for c in range(1,11):
    print('{} x {} = {}'.format(n1,c, c*n1))