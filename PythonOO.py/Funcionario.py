class Funcionario:
    def __init__(self, nome , salario):
        self.nome = nome
        self.salario = salario
    
    def aumentarSalario(self, porc):
        novo_salario =  self.salario + (self.salario * porc/100)
        print('O seu novo salario é: {}'.format(novo_salario))

harry = Funcionario("Harry", 10000)

harry.aumentarSalario(20)


