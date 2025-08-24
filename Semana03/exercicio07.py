class No:
    def __init__(self, nome, valor):
        self.nome = nome
        self.info = valor
        self.prox = None

def lista_insere_final(lst, nome, valor):
    novo = No(nome, valor)
    if lst is None:
        return novo
    aux = lst
    while aux.prox is not None:
        aux = aux.prox
    aux.prox = novo
    return lst

def lista_altera(lst):
    aux = lst
    while aux is not None:
        aux.info = -aux.info
        aux = aux.prox
    return lst

def mostra_lista(lst):
    aux = lst
    while aux is not None:
        print(f"{aux.nome}: {aux.info}", end=" -> " if aux.prox else "")
        aux = aux.prox
    print()

def main():
    lista = None
    while True:
        print("\nMENU")
        print("1 - Adicionar elemento")
        print("2 - Mostrar lista")
        print("3 - Inverter sinais")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do elemento: ")
            valor = int(input(f"Digite o valor de {nome}: "))
            lista = lista_insere_final(lista, nome, valor)
        elif opcao == "2":
            if lista is None:
                print("Lista vazia")
            else:
                mostra_lista(lista)
        elif opcao == "3":
            if lista is None:
                print("Lista vazia")
            else:
                lista_altera(lista)
                print("Sinais invertidos com sucesso!")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()
