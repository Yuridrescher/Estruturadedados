class No:
    def __init__(self, identificador, nome, nota):
        self.id = identificador
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None


def menu():
    print("\n--- MENU ---")
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Mostrar situação dos alunos")
    print("5 - Sair")
    return int(input("Escolha: "))


def main():
    cabeca = None

    while True:
        opc = menu()

        if opc == 1:  # Inserir
            id = input("ID: ")
            nome = input("Nome: ")
            nota = float(input("Nota: "))

            novo = No(id, nome, nota)
            if cabeca is None:
                cabeca = novo
                cabeca.proximo = cabeca
                cabeca.anterior = cabeca
            else:
                ultimo = cabeca.anterior
                ultimo.proximo = novo
                novo.anterior = ultimo
                novo.proximo = cabeca
                cabeca.anterior = novo

        elif opc == 2:  # Listar
            if cabeca is None:
                print("Lista vazia!")
            else:
                aux = cabeca
                while True:
                    print(f"ID: {aux.id} | Nome: {aux.nome} | Nota: {aux.nota}")
                    aux = aux.proximo
                    if aux == cabeca:
                        break

        elif opc == 3:  # Remover
            if cabeca is None:
                print("Lista vazia!")
            else:
                id_remover = input("Digite o ID para remover: ")
                aux = cabeca
                achou = False
                while True:
                    if aux.id == id_remover:
                        achou = True
                        if aux.proximo == aux:  # único nó
                            cabeca = None
                        else:
                            aux.anterior.proximo = aux.proximo
                            aux.proximo.anterior = aux.anterior
                            if aux == cabeca:
                                cabeca = aux.proximo
                        print("Aluno removido!")
                        break
                    aux = aux.proximo
                    if aux == cabeca:
                        break
                if not achou:
                    print("Aluno não encontrado!")

        elif opc == 4:  # Situação
            if cabeca is None:
                print("Lista vazia!")
            else:
                aux = cabeca
                while True:
                    if aux.nota >= 7:
                        situacao = "Aprovado"
                    elif aux.nota >= 4:
                        situacao = "Exame"
                    else:
                        situacao = "Reprovado"

                    print(f"ID: {aux.id} | Nome: {aux.nome} | Nota: {aux.nota} | {situacao}")

                    aux = aux.proximo
                    if aux == cabeca:
                        break

        elif opc == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


main()
