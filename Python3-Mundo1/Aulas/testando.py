#a =[1,2,3]

#a.append(4)
#print(a)

#a.extend([2,5,6])
#print(a)

#a.insert(3,4)
#print(a)

#a =[5,4,2,7,1]

#print('O item removido é: {} '.format(a.pop(2)))
#print('A lista agora esta assim: {}'.format(a))

#a.sort()
#print(a)

#dicionario = {
  #  "Nome" : "Sancho",
   # "Idade" : 20,
   # "Cidade" : "Pindai"
#}

#print(dicionario)

##def saudacoes(nome, escola):
   # print('Seja bem vindo {} voce esta na escola {} '.format(nome,escola))

#saudacoes("sancho","bahiano")


def calculadora(num1,num2,operacao):
    if operacao == 'soma':
        soma = num1 + num2
        print('O resultado da soma é: {}'.format(soma))
    elif operacao == 'divisao':
        divisao = num1 / num2
        print('O resultado da multiplicacao é: {}'.format(divisao))
    elif operacao == 'subtracao':
         subtracao = num1 - num2
         print('O resultado da subtracao é: {}'.format(subtracao))
    elif operacao == 'multiplicacao':
        multiplicacao = num1 * num2
        print('O resultado da multiplicacao é: {}'.format(multiplicacao))
    else:
        print('Boa sorte da proxima')

calculadora(10,5,'multiplicacao')
    