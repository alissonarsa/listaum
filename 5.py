import sys

# usamos um número muito grande para representar um caminho impossível (infinito)
INFINITO = sys.maxsize

def encontrar_caminho_minimo(mapa, inicio, fim):
    linhas = len(mapa)
    colunas = len(mapa[0])
    
    # cria uma matriz 'visitado' para não entrar em loops infinitos
    visitado = [[False for _ in range(colunas)] for _ in range(linhas)]
    
    inicio_x, inicio_y = inicio
    fim_x, fim_y = fim
    
    distancia = explorar(mapa, inicio_x, inicio_y, fim_x, fim_y, visitado)

    if distancia == INFINITO:
        return "Nenhum caminho encontrado."
    else:
        return f"O caminho mínimo tem {distancia} passos."

def explorar(mapa, x, y, fim_x, fim_y, visitado):
    
    # se sair do mapa, bater num muro, ou já tiver visitado este ponto
    if not (0 <= x < len(mapa) and 0 <= y < len(mapa[0])) or \
       mapa[x][y] == 1 or visitado[x][y]:
        return INFINITO
        
    # se chegar ao destino, o caminho a partir daqui tem 0 passos.
    if x == fim_x and y == fim_y:
        return 0
    
    # marca a posição atual como visitada para não voltar para ela no mesmo caminho
    visitado[x][y] = True
    
    # explora as 4 direções e pega o menor resultado
    caminho_baixo = explorar(mapa, x + 1, y, fim_x, fim_y, visitado)
    caminho_cima = explorar(mapa, x - 1, y, fim_x, fim_y, visitado)
    caminho_direita = explorar(mapa, x, y + 1, fim_x, fim_y, visitado)
    caminho_esquerda = explorar(mapa, x, y - 1, fim_x, fim_y, visitado)
    
    # desmarca a posição atual como visitada (IMPORTANTE para o backtracking)
    visitado[x][y] = False

    menor_caminho_dos_vizinhos = min(caminho_baixo, caminho_cima, caminho_direita, caminho_esquerda)
    
    if menor_caminho_dos_vizinhos == INFINITO:
        return INFINITO
    
    return menor_caminho_dos_vizinhos + 1

mapa_exemplo = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

ponto_inicial = (0, 0)
ponto_final = (3, 3)

print(encontrar_caminho_minimo(mapa_exemplo, ponto_inicial, ponto_final))



