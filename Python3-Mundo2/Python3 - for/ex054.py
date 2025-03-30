
minha_lista = []
for ano in range(1, 8):
    nascimento = int(input('Data de nascimento: '))
    minha_lista.append(nascimento)

atingiram = 0
naoatingiram = 0
idade = 0
for numero in minha_lista:
    idade =  2025 - numero
    if idade > 18:
        atingiram += 1
    else:
        naoatingiram += 1

print('{} pessoas sao de maiores'.format(atingiram))
print('{} pessoas NAO SAO de maiores'.format(naoatingiram))



    



#for nascimento in range(1,8):
  #  print(nascimento)
