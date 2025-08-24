class No:
    def __init__(self, nome, valor):
        self.nome = nome
        self.info = valor
        self.prox = None

def lista_insere_final(lst, nome, valor):
    novo = No(nome, valor)
    if lst == None:
        return novo
    aux = lst
    while aux.prox != None:
        aux = aux.prox
    aux.prox = novo
    return lst

def mostra(lista):
    aux = lista
    while aux != None:
        print(f"{aux.nome}: {aux.info}", end=" -> " if aux.prox else "")
        aux = aux.prox
    print()

def main():
    lista = None
    qtd = int(input("Quantos elementos deseja inserir? "))
    for i in range(qtd):
        nome = input(f"Digite o nome do elemento {i+1}: ")
        valor = int(input(f"Digite o valor de {nome}: "))
        lista = lista_insere_final(lista, nome, valor)
    print("Lista final:")
    mostra(lista)

main()
