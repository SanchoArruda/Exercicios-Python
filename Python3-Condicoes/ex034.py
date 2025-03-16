salario = int(input('Qual o valor do seu salario: '))

if salario > 1250:
    aumento = (salario * 0.10)+salario
    print('O seu salario novo eh: {}'.format(aumento))
else:
    aumento2 = (salario * 0.15)+salario
    print('O seu salario novo eh: {}'.format(aumento2))