import os

# 1
diretorio = r"C:\Users\aliss\Documents\GitHub\listaum\listaum"

def explorar_diretorio(caminho):
    print(f"Explorando: {caminho}")
    
    try:
        itens = os.listdir(caminho) #listdir: pega a lista de todos os itens de diretorio

        for item in itens:
            caminhocompleto = os.path.join(caminho, item)

            if os.path.isdir(caminhocompleto): #isdir: verifica se é diretório (pasta)
                print(f"  -> [PASTA] {item}")
                explorar = explorar_diretorio(caminhocompleto)
            else:
                print(f"  -> [ARQUIVO] {item}")

    except PermissionError:
        print(f"Não foi possivel acessar: {caminho}")

explorar_diretorio(diretorio)