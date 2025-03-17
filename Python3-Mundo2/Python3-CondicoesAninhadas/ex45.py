import random 

print('---------------VAI COMECAR O JOGO------------------')
escolha = str(input('Escolha Pedra , Papel ou Tesoura: '))

jokenpo = {"Pedra",'Papel', 'Tesoura'}

sorteio = random.choice(list(jokenpo))

if escolha == "Tesoura":
    if sorteio == 'Papel':
        print('Parabens Tesoura ganhou')
    elif sorteio == 'Pedra':
        print('Voce perdeu')
    else:
        print('Empatou')
elif escolha == "Pedra":
    if sorteio == 'Papel':
        print('Voce perdeu')
    elif sorteio == 'Pedra':
        print('EMPATOU')
    else:
        print('Parabens voce ganhou')
elif escolha == 'Papel':
    if sorteio == 'Papel':
        print('EMPATOU')
    elif sorteio == 'Pedra':
        print('Voce ganhou')
    else:
        print('Voce perdeu')


print("-----------------------------------------")
print('O numero sorteado foi {}'.format(sorteio))