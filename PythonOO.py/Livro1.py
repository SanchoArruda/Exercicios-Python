class Livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
         print('O preco é: {}'.format(self.preco))
        
    
    def setPreco(self, novo_preco):
        if self.preco > 0 :
            self.preco = novo_preco
            print('O preco alterou para: {}'.format(self.preco))
        else:
            print("Erro: O preço deve ser maior que 0")

livro1 = Livro('Jardim Paraiso', 200, 'Sancho Arruda', 100)

livro1.getPreco()

livro1.setPreco(104)
livro1.getPreco()
livro1.getPreco()

livro1.setPreco(107)

        