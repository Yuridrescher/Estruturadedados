class Musica:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None


print("Playlist de músicas")
cabeca = None
atual = None

while True:
    print("\n1 - Adicionar música")
    print("2 - Listar músicas")
    print("3 - Remover música")
    print("4 - Buscar música")
    print("5 - Mostrar duração total")
    print("6 - Próxima música")
    print("7 - Música anterior")
    print("8 - Sair")
    opc = int(input("Opção: "))

    if opc == 1:
        id = input("ID: ")
        nome = input("Nome: ")
        artista = input("Artista: ")
        duracao = float(input("Duração (min): "))
        nova = Musica(id, nome, artista, duracao)

        if cabeca == None:
            cabeca = nova
            cabeca.proximo = cabeca
            cabeca.anterior = cabeca
            atual = cabeca
        else:
            ultimo = cabeca.anterior
            ultimo.proximo = nova
            nova.anterior = ultimo
            nova.proximo = cabeca
            cabeca.anterior = nova

        print("Música adicionada!")

    elif opc == 2:
        if cabeca == None:
            print("Playlist vazia")
        else:
            aux = cabeca
            while True:
                print(f"{aux.id} - {aux.nome} - {aux.artista} - {aux.duracao} min")
                aux = aux.proximo
                if aux == cabeca:
                    break

    elif opc == 3:
        if cabeca == None:
            print("Playlist vazia")
        else:
            id_remover = input("ID da música: ")
            aux = cabeca
            achou = False
            while True:
                if aux.id == id_remover:
                    achou = True
                    if aux.proximo == aux:
                        cabeca = None
                        atual = None
                    else:
                        aux.anterior.proximo = aux.proximo
                        aux.proximo.anterior = aux.anterior
                        if aux == cabeca:
                            cabeca = aux.proximo
                        if aux == atual:
                            atual = aux.proximo
                    print("Música removida")
                    break
                aux = aux.proximo
                if aux == cabeca:
                    break
            if not achou:
                print("Não encontrada")

    elif opc == 4:
        if cabeca == None:
            print("Playlist vazia")
        else:
            termo = input("Digite nome ou artista: ")
            aux = cabeca
            achou = False
            while True:
                if aux.nome == termo or aux.artista == termo:
                    print(f"{aux.id} - {aux.nome} - {aux.artista} - {aux.duracao} min")
                    achou = True
                aux = aux.proximo
                if aux == cabeca:
                    break
            if not achou:
                print("Nada encontrado")

    elif opc == 5:
        if cabeca == None:
            print("Playlist vazia")
        else:
            total = 0
            aux = cabeca
            while True:
                total += aux.duracao
                aux = aux.proximo
                if aux == cabeca:
                    break
            print("Duração total:", total, "minutos")

    elif opc == 6:
        if atual == None:
            print("Playlist vazia")
        else:
            atual = atual.proximo
            print("Tocando agora:", atual.nome, "-", atual.artista)

    elif opc == 7:
        if atual == None:
            print("Playlist vazia")
        else:
            atual = atual.anterior
            print("Tocando agora:", atual.nome, "-", atual.artista)

    elif opc == 8:
        print("Saindo...")
        break

    else:
        print("Opção inválida")
