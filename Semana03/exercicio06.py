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

def lista_calcula_media(lst):
    if lst is None:
        return 0
    soma = 0
    cont = 0
    aux = lst
    while aux is not None:
        soma += aux.info
        cont += 1
        aux = aux.prox
    return soma / cont

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
        print("3 - Calcular média")
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
                print("Lista vazia, média = 0")
            else:
                media = lista_calcula_media(lista)
                print(f"Média dos valores: {media:.2f}")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()
