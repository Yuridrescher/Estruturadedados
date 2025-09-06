class Tarefa:
    def __init__(self, descricao, prazo):
        self.descricao = descricao
        self.prazo = prazo
        self.proximo = None
        self.anterior = None


def inserir_tarefa(cabeca, descricao, prazo):
    nova = Tarefa(descricao, prazo)
    if cabeca is None:
        cabeca = nova
    else:
        nova.proximo = cabeca
        cabeca.anterior = nova
        cabeca = nova
    return cabeca


def remover_tarefa(cabeca, descricao):
    if cabeca is None:
        print("Lista vazia")
        return cabeca

    aux = cabeca
    while aux is not None:
        if aux.descricao == descricao:
            if aux.anterior is not None:
                aux.anterior.proximo = aux.proximo
            else:
                cabeca = aux.proximo
            if aux.proximo is not None:
                aux.proximo.anterior = aux.anterior
            print("Tarefa removida:", descricao)
            return cabeca
        aux = aux.proximo

    print("Tarefa não encontrada:", descricao)
    return cabeca


def listar_tarefas(cabeca):
    if cabeca is None:
        print("Nenhuma tarefa cadastrada")
        return

    aux = cabeca
    print("\n--- Lista de Tarefas ---")
    while aux is not None:
        print(f"- {aux.descricao} (prazo: {aux.prazo})")
        aux = aux.proximo


def menu():
    print("\n--- MENU ---")
    print("1 - Inserir nova tarefa")
    print("2 - Remover tarefa existente")
    print("3 - Listar todas as tarefas")
    print("4 - Sair")
    return int(input("Opção: "))


def main():
    cabeca = None
    while True:
        opc = menu()
        if opc == 1:
            desc = input("Descrição: ")
            prazo = input("Prazo: ")
            cabeca = inserir_tarefa(cabeca, desc, prazo)
        elif opc == 2:
            desc = input("Descrição da tarefa a remover: ")
            cabeca = remover_tarefa(cabeca, desc)
        elif opc == 3:
            listar_tarefas(cabeca)
        elif opc == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
