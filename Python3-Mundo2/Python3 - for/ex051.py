pt = int(input('Escreva o primeiro termo: '))
pa = int(input('Escreva a razão de uma PA: '))

soma = 0
for c in range(1, 11): 
    soma = pt + (c-1)*pa
    print('A posicao do termo: {} Primeiro termo {} e e raza : {} a PA é : {}'.format(c, pt, pa, soma))