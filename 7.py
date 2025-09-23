def criar_teatro(fileiras, colunas):
    return [[0 for _ in range(colunas)] for _ in range(fileiras)]

def mostrar_teatro(teatro):
    print("\n--- MAPA DO TEATRO (0 = Vazio, 1 = Ocupado) ---")
    print("   " + " ".join([str(i) for i in range(len(teatro[0]))]))
    print("  " + "-" * (len(teatro[0]) * 2))

    for i, fileira in enumerate(teatro):
        print(f"{i}| ", end="") 
        print(" ".join(map(str, fileira)))
    print("-" * 35)

def reservar_assento(teatro, fileira, coluna):
    if not (0 <= fileira < len(teatro) and 0 <= coluna < len(teatro[0])):
        print("Erro: Assento inválido. Fora dos limites do teatro.")
        return False
        
    if teatro[fileira][coluna] == 1:
        print("Erro: Este assento já está ocupado.")
        return False
        
    teatro[fileira][coluna] = 1
    print(f"Sucesso! Assento na fileira {fileira}, coluna {coluna} reservado.")
    return True

NUM_FILEIRAS = 5
NUM_COLUNAS = 10
teatro = criar_teatro(NUM_FILEIRAS, NUM_COLUNAS)

while True:
    mostrar_teatro(teatro)
    
    try:
        entrada = input("Digite a fileira e a coluna para reservar (ex: 2 5), ou 'sair': ")
        
        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break
            
        fileira_desejada = int(entrada.split()[0])
        coluna_desejada = int(entrada.split()[1])
        
        reservar_assento(teatro, fileira_desejada, coluna_desejada)

    except (ValueError, IndexError):
        print("Entrada inválida. Por favor, digite dois números separados por espaço.")