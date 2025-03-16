ano = int(input('Escreva o ano que quer: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano {} eh bissexto".format(ano))
else:
    print('O ano não eh bissexto')
    