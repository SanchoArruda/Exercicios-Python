preco = float(input('Escreva o valor do produto: '))
condicao = int(input('Como deseja pagar? (1) Á vista , (2) Á vista no cartão, (3) Em até 2x Cartão, (4) 3x ou mais no cartão: '))

if condicao == 1: 
    desconto = (preco * (10/100))
    acs_desconto = preco - desconto
    print('Seu desconto é: {}'.format(desconto))
    print('O valor com o desconto é: {} à vista no dinheiro'.format(acs_desconto))
elif condicao == 2:
    desconto = (preco * (5/100))
    acs_desconto = preco - desconto
    print('Seu desconto é: {} '.format(desconto))
    print('O valor com o desconto é: {} no cartão à vista'.format(acs_desconto))
elif condicao == 3:
    print('Voce não tem desconto em 2x no cartão o valor é: {}'.format(preco))
elif condicao == 4:
    juros = (preco * (20/100))
    acs_juros = preco + juros
    print('Seu juros é: {} '.format(juros))
    print('O valor com o juros é: {} no cartão 3x'.format(acs_juros))
else: 
    print('O numero digitado não corresponde, coloque algum que esta entre ( )')