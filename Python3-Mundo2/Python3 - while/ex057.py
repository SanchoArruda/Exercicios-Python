
s1 = ''
while s1 != 'M' and s1 != 'F': 
    s1 = str(input('Digite o seu sexo:(F/M): ')).upper()
    if s1 != 'M' and s1 != 'F':
        print('Digitou sem F/M, digite nesse formato')
    else: 
        print('Parabens voce é inteligente o sufiente! kk')
print('FIM')
