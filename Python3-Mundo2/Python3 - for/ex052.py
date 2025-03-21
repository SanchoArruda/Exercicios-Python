numero = int(input('Escreva um numero e confira se é primo: '))

for i in range(2, numero+1):
    if numero % i == 0 and numero % numero == 0:
        return True
    else: 

print(numero)
    
   
