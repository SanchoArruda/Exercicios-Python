try:
    x = int(input("X: "))
    y = int(input("Y: "))
    soma = x / y
    print(soma)
    
except ZeroDivisionError:
    print("Erro divisao! Esta divindo por 0")
    
