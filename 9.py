def mostrar_agenda(agenda):
    print("\n--- Agenda Telefônica ---")
    if not agenda:
        print("A agenda está vazia.")
    else:
        # O método .items() nos dá a chave e o valor de cada item no dicionário
        for nome, telefone in agenda.items():
            print(f" - Nome: {nome}, Telefone: {telefone}")
    print("-" * 25)

def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print(f"Contato '{nome}' adicionado/atualizado com sucesso!")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print(f"Erro: Contato '{nome}' não encontrado.")

def buscar_contato(agenda, nome):
    telefone = agenda.get(nome)
    if telefone:
        print(f"Telefone de '{nome}': {telefone}")
    else:
        print(f"Contato '{nome}' não encontrado.")



agenda_telefonica = {}

while True:
    print("\nOpções:")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Mostrar todos")
    print("5. Sair")
    
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(agenda_telefonica, nome, telefone)
    
    elif escolha == '2':
        nome = input("Digite o nome do contato a ser removido: ")
        remover_contato(agenda_telefonica, nome)

    elif escolha == '3':
        nome = input("Digite o nome do contato a ser buscado: ")
        buscar_contato(agenda_telefonica, nome)

    elif escolha == '4':
        mostrar_agenda(agenda_telefonica)

    elif escolha == '5':
        print("Encerrando o programa.")
        break
        
    else:
        print("Opção inválida. Tente novamente.")