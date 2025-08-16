class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

aluno1 = Aluno("Matheus", [8, 7, 9])
aluno2 = Aluno("Davi", [10, 9, 8])
aluno3 = Aluno("Roberto", [6, 5, 7])

turma = [aluno1, aluno2, aluno3]

for aluno in turma:
    print(f"Aluno: {aluno.nome} | Média: {aluno.media():.2f}")
