nome = input('Escreva seu nome: ').strip()


#print(nome.split()[0]) #primeiro nome

#print(nome.split()[-1]) #ultimo nome

n = nome.split()  #PRIMEIRA FORMA
print(n)
print(n[len(n)-1])


                        #SEGUNDA FORMA
print('O seu primeiro nome eh: {}'.format(nome.split()[0]))
print('O seu último nome eh:  {}'.format(nome.split()[-1]))
