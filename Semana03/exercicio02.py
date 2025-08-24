class No:
    def __init__(self, info):
        self.info = info
        self.prox = None

def inserir_no_final(lst, valor):
    novo = No(valor)
    if lst is None:
        return novo
    else:
        atual = lst
        while atual.prox is not None:
            atual = atual.prox
        atual.prox = novo
        return lst

def maiores(lst, n):
    atual = lst  
    contador = 0
    while atual is not None:
        if atual.info > n:
            contador += 1
        atual = atual.prox 
    return contador

def imprimir_lista(lst):
    atual = lst
    while atual is not None:
        print(atual.info, end=" -> " if atual.prox else "")
        atual = atual.prox
    print()

def main():
    lista = None
    qtd = int(input("Quantos nós deseja inserir? "))
    for i in range(qtd):
        valor = int(input(f"Digite o valor do nó {i+1}: "))
        lista = inserir_no_final(lista, valor)
    imprimir_lista(lista)
    n = int(input("Digite o valor limite: "))
    print(maiores(lista, n))

if __name__ == "__main__":
    main()
