class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []
        
    def cadastrarnota(self, nota):
        self.notas.append(nota)
    
    def mostrarnotas(self):
        return self.notas
    
    def medianotas(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_situacao(self):
        if self.medianotas() < 7:
            return "Reprovado"
        else:
            return "Aprovado"

matheus = Aluno("Matheus", 20)
matheus.cadastrarnota(10)
matheus.cadastrarnota(8)
matheus.cadastrarnota(7)


print("Notas do", matheus.nome, ":", matheus.mostrarnotas())
print("Média:", matheus.medianotas())
print("Situação:", matheus.verificar_situacao())
