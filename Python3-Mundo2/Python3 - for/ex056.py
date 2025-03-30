nomes = []
idades = []
sexos = []
for leia in range(1,6):

    nome = str(input('\nEscreva seu nome: '))
    nomes.append(nome)

    idade = int(input('Escreva sua idade: '))
    idades.append(idade)

    sexo = str(input('Escreva seu sexo: ')).upper()
    sexos.append(sexo)

media = 0
qtd_numero = 0
soma = 0 
for numero in idades:
    qtd_numero += 1
    soma += numero
    media = soma/qtd_numero

count = 0
for i in range(len(sexos)):
    if sexos[i] == 'FEMININO' and idades[i] < 20:
            count += 1

maior = idades[0]
nomeMaior = nomes[0]
for i in range(len(idades)):
    if sexos[i] == 'MASCULINO':
         if idades[i] > maior:
              maior = idades[i]
              nomeMaior = nomes[i] 


print('\nA idade maior do homem é: {} e seu nome é: {}'.format(maior,nomeMaior))
print('{} mulheres tem menos de 20 anos'.format(count))
print('A media de idade do grupo é: {}\n'.format(media))




    
