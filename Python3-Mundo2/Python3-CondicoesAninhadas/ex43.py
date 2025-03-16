altura = float(input('Escreva a sua altura: '))
peso = float(input('Escreva o seu peso: '))

imc = peso / (altura ** 2)      #ou pow(altura,2)

print('Seu IMC eh de: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você esta abaixo do peso! ')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbita')
    