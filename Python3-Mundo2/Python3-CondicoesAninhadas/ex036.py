casa = float(input('Escreva o valor da casa: ')) #10.000
salario = float(input('Escreva o seu salario: ')) #1.000
anos = int(input('Quantos anos vai pagar: '))  #2 anos


total_mes = anos*12     # 1 ano tem 12 meses , quero saber a quantidade em meses aqui
valor_pago_mes = casa/total_mes  #o valor que irei pagar em meses.

porc = (salario*0.30)      # qtd que o salario sera pago


if valor_pago_mes > porc:
    print('Não podera pegar o emprestimo')
elif valor_pago_mes < porc:
    print('Voce pode pegar o emprestimo!')
print('-------------------------------------------------------------')
print('O valor do emprestimo esta: {:.2f} por mes'.format(valor_pago_mes))
print('O valor limite é de: {:.2f} reais por mes'.format(porc))



