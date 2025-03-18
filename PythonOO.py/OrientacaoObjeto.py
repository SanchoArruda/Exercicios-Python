class ContBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print("O deposito foi feito {}".format(valor))

    def sacar(self, saque):
        if saque > self.saldo:
            print('Saldo insuficiente para saque')
        else:
            self.saldo -= saque
        print('O saque de {} , foi feito'.format(saque))

    def exibir_saldo(self):
         print("Saldo atual de {}: R${:.2f}".format(self.titular, self.saldo))

conta1 = ContBancaria("Sancho")

conta1.depositar(50)

conta1.sacar(200)

conta1.exibir_saldo()