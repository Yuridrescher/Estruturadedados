class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

contato1 = Contato("Augusto", 1111, "augusto@gmail.com")
contato2 = Contato("Davi", 2222, "davi@hotmail.com")
contato3 = Contato("Otavio", 3333, "otavio@edu.com")

agenda = [contato1, contato2, contato3]

for contato in agenda:
    print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, email: {contato.email}")
