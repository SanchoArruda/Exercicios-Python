class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        soma = self.ladoA + self.ladoB + self.ladoC
        print('O perimetro é: {}'.format(soma))

    def getMaiorLado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print('O maior lado é: {}'.format(self.ladoA))
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print('O maior lado é: {}'.format(self.ladoB))
        elif self.ladoC > self.ladoB and self.ladoC > self.ladoA:
            print('O maior lado é: {}'.format(self.ladoC))
        else: 
            print('Nenhum lado kkk')
        
n1 = int(input('Escreva o ladoA: '))
n2 = int(input('Escreva o ladoB: '))
n3 = int(input('Escreva o ladoC: '))

cal = Triangulo(n1,n2,n3)

cal.calcular_perimetro()

cal.getMaiorLado()



