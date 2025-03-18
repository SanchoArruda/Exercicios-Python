class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivel_combustivel = 0.0

    def andar(self, distancia):
        gasto = distancia / self.consumo
        self.nivel_combustivel -= gasto

    def adicionarGasolina(self, qtdAbastecer):
        self.nivel_combustivel += qtdAbastecer

    def obterGasolina(self):
        print("O nivel de gasolina é: {}".format(self.nivel_combustivel))


Corola = Carro(10)

Corola.adicionarGasolina(11)

Corola.andar(100)

Corola.obterGasolina()

Corola.adicionarGasolina(10)

Corola.obterGasolina()

Corola.adicionarGasolina(10)

Corola.obterGasolina()