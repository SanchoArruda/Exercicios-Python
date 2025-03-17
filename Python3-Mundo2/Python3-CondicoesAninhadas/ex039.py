from datetime import date

nascimento = int(input('Ano de nascimento seu: '))
ano_atual = date.today().year 

idade = ano_atual - nascimento

if idade == 18:
    print('Hora de se alistar')
elif idade < 18:
    print('Ainda vai se alistar')
    print('Falta {} anos para voce se alistar'.format(18-idade))
else: 
    print('Ja passou do tempo')
    print('Ja passou {} anos que era para voce se alistar'.format(idade-18))

print('Voce tem {} anos'.format(idade))


