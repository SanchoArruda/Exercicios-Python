from datetime import date

ano = int(input('Escreva o ano que quer(digite 0 se for calcular o atual): '))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano {} eh bissexto".format(ano))
else:
    print('O ano não eh bissexto')
