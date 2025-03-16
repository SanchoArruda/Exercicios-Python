n1 = float(input('Escreva o novo preco a ser calculado: R$'))

novoP = n1 - (n1 * 5/100)

print('O preco inicial é: {:.2f} e o preco com ajuste de 5%  o valor final fica: {:.2f}'.format(n1, novoP))