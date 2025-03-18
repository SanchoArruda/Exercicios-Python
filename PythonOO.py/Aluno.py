class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, qtdHorasEstudo):
        self.tempoSemDormir += qtdHorasEstudo

        print('A qtd de horas acumuladas sem dormir foi de: {}'.format(self.tempoSemDormir))

aluno1 = Aluno('Sancho', 'ADS', 2)

aluno1.estudar(10)

        