n1 = float(input('Escreva a primeira nota: '))
n2 = float(input('Escreva a segunda nota: '))

media = (n1 + n2) / 2

print('A media do aluno eh {}'.format(media))
if media < 5:
    print('Voce foi reprovado')
elif media >= 5 and media < 7:
    print('Recuperacao')
elif media >= 7: 
    print('Aprovado')
else: 
    print('Voce colocou um numero errado')
