class No:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

def ultimo(lista):
    if lista == None:
        return None
    aux = lista
    while aux.prox != None:
        aux = aux.prox
    return aux

def main():
    lista = None
    qtd = int(input("Quantos nós quer inserir? "))
    for i in range(qtd):
        val = int(input("Digite o valor: "))
        novo = No(val)
        if lista == None:
            lista = novo
        else:
            aux = lista
            while aux.prox != None:
                aux = aux.prox
            aux.prox = novo

    ult = ultimo(lista)
    if ult != None:
        print("Último nó é:", ult.info)
    else:
        print("Lista está vazia")

main()
