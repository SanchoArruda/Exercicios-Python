
pt = int(input('Escreva o primeiro termo de uma PA: '))
pa = int(input('Escreva a razao de uma PA: '))

print('Os 10 primeiros termos dessa PA é: \n')
n = 1
while n <= 10:
    calc = pt + (n-1)*pa 

    print(calc)
    n += 1

r = ''
while r != 0:
    r = int(input('Digite quantos termos voce quer a mais (0 voce sai do app): '))

    n = 1
    while n <= r:
        calc = pt + (n-1)*pa 
        print(calc)
        n += 1