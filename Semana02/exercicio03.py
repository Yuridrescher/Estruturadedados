class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, valor):
        self.quantidade += valor

    def mostrar_dados(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")
        


produto1 = Produto("Notebook", 5000.00, 3)
produto2 = Produto("Celular", 2000.00, 2)

print("Antes da atualização:")
produto1.mostrar_dados()
produto2.mostrar_dados()

produto1.atualizar_estoque(5)  
produto2.atualizar_estoque(3)   

print("Depois da atualização:")
produto1.mostrar_dados()
produto2.mostrar_dados()
