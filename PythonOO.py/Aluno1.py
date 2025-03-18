class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_info(self):
        print("Nome: {} | CPF: {}".format(self.nome, self.cpf))

class Equipe:
    def __init__(self, projeto):
        self.projeto = projeto
        self.participantes = []  

    def adicionar_participante(self, aluno):
        if isinstance(aluno, Aluno):
            self.participantes.append(aluno)
        else:
            print("O participante precisa ser um objeto da classe Aluno.")

    def exibir_participantes(self):
        print("Participantes do projeto {}:".format(self.projeto))
        for aluno in self.participantes:
            aluno.exibir_info()

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    def criarEquipe(self, nome_projeto, lista_alunos):
        for equipe in self.equipes:
            if equipe.projeto == nome_projeto:
                for aluno in lista_alunos:
                    for participante in equipe.participantes:
                        if aluno.cpf == participante.cpf:
                            print("A equipe com o projeto {} não pode ser criada, pois o aluno {} já está em outra equipe com este projeto.".format(nome_projeto, aluno.nome))
                            return

        nova_equipe = Equipe(nome_projeto)
        for aluno in lista_alunos:
            nova_equipe.adicionar_participante(aluno)
        self.equipes.append(nova_equipe)
        print("A equipe com o projeto {} foi criada com sucesso!".format(nome_projeto))

    def exibir_equipes(self):
        if not self.equipes:
            print("Nenhuma equipe foi formada ainda.")
        for equipe in self.equipes:
            equipe.exibir_participantes()

aluno1 = Aluno("João", "12345678901")
aluno2 = Aluno("Maria", "10987654321")
aluno3 = Aluno("Carlos", "98765432100")
aluno4 = Aluno("Ana", "19283746501")

gerenciador = GerenciadorEquipes()

gerenciador.criarEquipe("Projeto A", [aluno1, aluno2])
gerenciador.criarEquipe("Projeto B", [aluno3, aluno4])

gerenciador.criarEquipe("Projeto A", [aluno2, aluno3])  

gerenciador.exibir_equipes()
