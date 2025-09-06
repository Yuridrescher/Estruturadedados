class No:
    def __init__(self, identificador, nome):
        self.id = identificador
        self.nome = nome
        self.proximo = None
        self.anterior = None


def menu():
    print("\n--- MENU ---")
    print("1 - Inserir nó")
    print("2 - Remover nó")
    print("3 - Listar nós")
    print("4 - Verificar se nó existe")
    print("5 - Sair")
    opc = int(input("Digite a opção: "))
    return opc


def inserirNo(cabeca, identificador, nome):
    novo = No(identificador, nome)

    if cabeca is None:
        cabeca = novo
        cabeca.proximo = cabeca
        cabeca.anterior = cabeca
        return cabeca

    ultimo = cabeca.anterior

    ultimo.proximo = novo
    novo.anterior = ultimo
    novo.proximo = cabeca
    cabeca.anterior = novo

    return cabeca


def listarNos(cabeca):
    if cabeca is None:
        print("Lista vazia!")
        return

    aux = cabeca
    while True:
        print(f"ID: {aux.id} | Nome: {aux.nome}")
        aux = aux.proximo
        if aux == cabeca:
            break


def removerNo(cabeca, identificador):
    if cabeca is None:
        print("Lista vazia!")
        return None

    aux = cabeca
    while True:
        if aux.id == identificador:
            # Caso seja o único nó
            if aux.proximo == aux and aux.anterior == aux:
                print(f"Nó {identificador} removido. Lista ficou vazia.")
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == cabeca:  # removendo a cabeça
                cabeca = aux.proximo

            print(f"Nó {identificador} removido com sucesso!")
            return cabeca

        aux = aux.proximo
        if aux == cabeca:
            print("Identificador não encontrado!")
            return cabeca


def verificarNo(cabeca):
    if cabeca is None:
        print("Lista vazia!")
        return

    print("Verificar por:\n1 - Nome\n2 - Identificador")
    opc = input("Opção: ")

    if opc == "1":
        nome = input("Digite o nome: ")
        aux = cabeca
        while True:
            if aux.nome == nome:
                print(f"Nó encontrado -> ID: {aux.id}, Nome: {aux.nome}")
                return
            aux = aux.proximo
            if aux == cabeca:
                break
        print("Nome não encontrado!")

    elif opc == "2":
        identificador = input("Digite o identificador: ")
        aux = cabeca
        while True:
            if str(aux.id) == identificador:
                print(f"Nó encontrado -> ID: {aux.id}, Nome: {aux.nome}")
                return
            aux = aux.proximo
            if aux == cabeca:
                break
        print("Identificador não encontrado!")
    else:
        print("Opção inválida!")


def main():
    cabeca = None
    opc = 0

    while opc != 5:
        opc = menu()

        if opc == 1:
            identificador = input("Digite o identificador: ")
            nome = input("Digite o nome: ")
            cabeca = inserirNo(cabeca, identificador, nome)

        elif opc == 2:
            identificador = input("Digite o identificador para remover: ")
            cabeca = removerNo(cabeca, identificador)

        elif opc == 3:
            listarNos(cabeca)

        elif opc == 4:
            verificarNo(cabeca)

        elif opc == 5:
            print("Saindo...")

        else:
            print("Opção inválida!")


main()
