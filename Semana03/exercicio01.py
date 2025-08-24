class No:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

def lista_insere_final(lst, valor):
    novo = No(valor)
    if lst is None:
        return novo
    aux = lst
    while aux.prox is not None:
        aux = aux.prox
    aux.prox = novo
    return lst

def mostra_lista(lst):
    aux = lst
    if aux is None:
        print("Lista vazia")
        return
    while aux is not None:
        print(aux.info, end=" -> " if aux.prox else "")
        aux = aux.prox
    print()

def lista_remove_valor(lst, valor):
    if lst is None:
        return lst
    while lst is not None and lst.info == valor:
        lst = lst.prox
    aux = lst
    while aux is not None and aux.prox is not None:
        if aux.prox.info == valor:
            aux.prox = aux.prox.prox
        else:
            aux = aux.prox
    return lst

def main():
    lista = None
    while True:
        print("\nMENU")
        print("1 - Inserir item")
        print("2 - Listar itens")
        print("3 - Remover item")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor float: "))
            lista = lista_insere_final(lista, valor)
        elif opcao == "2":
            mostra_lista(lista)
        elif opcao == "3":
            valor = float(input("Digite o valor a remover: "))
            lista = lista_remove_valor(lista, valor)
            print(f"Valores {valor} removidos, se existiam.")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()
