class No:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

def insere_final(lista, valor):
    novo = No(valor)
    if lista == None:
        return novo
    aux = lista
    while aux.prox != None:
        aux = aux.prox
    aux.prox = novo
    return lista

def concatena(l1, l2):
    if l1 == None:
        return l2
    aux = l1
    while aux.prox != None:
        aux = aux.prox
    aux.prox = l2
    return l1

def mostra(lista):
    aux = lista
    while aux != None:
        print(aux.info, end=" -> " if aux.prox else "")
        aux = aux.prox
    print()

def cria_lista():
    lista = None
    qtd = int(input("Quantos nós quer inserir? "))
    for i in range(qtd):
        val = int(input("Digite o valor: "))
        lista = insere_final(lista, val)
    return lista

def main():
    print("Criando lista 1:")
    l1 = cria_lista()
    print("Criando lista 2:")
    l2 = cria_lista()
    print("Lista 1:")
    mostra(l1)
    print("Lista 2:")
    mostra(l2)
    l3 = concatena(l1, l2)
    print("Lista concatenada:")
    mostra(l3)

main()
