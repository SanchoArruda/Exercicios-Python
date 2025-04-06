sair = 0
while sair != 5:
    n1 = int(input('Escreva o primeiro numero: '))
    n2 = int(input('Esvreva o segundo numero: '))


    entrada = int(input('\nEsvreva o que voce quer\n\n[1] somar' \
    '[2] multiplicar\n' \
    '[3] maior' \
    '[4] novos números\n' \
    '[5] sair do programa\n\n' \
    'Digite aqui: '))

    mult = 0
    soma = 0 
    if entrada == 1:
        soma = n1 + n2
        print('\nA soma dos numeros {} + {} = {}'.format(n1,n2, soma))

    if entrada == 2:
        mult = n1 * n2
        print('A multiplicação dos numeros {} x {} = {}\n'.format(n1,n2, mult))

    maior = 0
    if entrada == 3:
        if n1 > n2:
            maior = n1
            print('O maior numero entre os dois é: {}'.format(maior))
        else:
            maior = n2
            print('O maior numero entre os dois é: {}'.format(maior))

    if entrada == 4:
        print('NOVOS NUMEROS: ')

    if entrada == 5:
        sair = 5


