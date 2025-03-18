class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = True

    def emprestar(self):
        if self.status == True:
            print('O livro foi emprestado')
            self.status = False
    def devolver(self):
        if self.status == False:
            print('O livro foi devolvido')
            self.status = True
    def exibir_info(self):

        print('Titulo: {} , Autor: {} , Status: {}'.format(self.titulo, self.autor, self.status))
        

livro1 = Livro("Python para Iniciantes", "Autor A")
livro2 = Livro("Aprendendo POO", "Autor B")


livro1.exibir_info()
livro2.exibir_info()

livro1.emprestar()

livro1.exibir_info()