class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

produto = Produto(nome, preco, quantidade)
print("Total em estoque do produto:", produto.calcular_total())
