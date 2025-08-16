class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def bonus(self):
        if self.cargo.lower() == "gerente":
            self.salario += self.salario * 0.10
        else:
            self.salario += self.salario * 0.05

ocupacao1 = Funcionario("Alan", 2000.00, "operador") 
ocupacao2 = Funcionario("Moises", 15000.00, "Gerente")

print(f"Nome: {ocupacao1.nome} salario: {ocupacao1.salario} cargo: {ocupacao1.cargo}")
print(f"Nome: {ocupacao2.nome} salario: {ocupacao2.salario} cargo: {ocupacao2.cargo}")

ocupacao1.bonus()
ocupacao2.bonus()

print(f"\nApós bônus:")
print(f"Nome: {ocupacao1.nome} salario: {ocupacao1.salario} cargo: {ocupacao1.cargo}")
print(f"Nome: {ocupacao2.nome} salario: {ocupacao2.salario} cargo: {ocupacao2.cargo}")
