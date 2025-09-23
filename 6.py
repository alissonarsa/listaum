def torres_de_hanoi(n, haste_origem, haste_destino, haste_auxiliar):
    
    # Se só temos 1 disco para mover, a tarefa é simples
    if n == 1:
        print(f"Mova o disco 1 da haste {haste_origem} para a haste {haste_destino}")
        return
    
    # Mover a pilha de n-1 discos da haste de Origem para a haste Auxiliar, usando a de Destino como apoio
    torres_de_hanoi(n - 1, haste_origem, haste_auxiliar, haste_destino)

    # Mover o disco maior (que sobrou na base) da haste de Origem para a de Destino
    print(f"Mova o disco {n} da haste {haste_origem} para a haste {haste_destino}")

    # Mover a pilha de n-1 discos da haste Auxiliar para a haste de Destino, usando a de Origem como apoio
    torres_de_hanoi(n - 1, haste_auxiliar, haste_destino, haste_origem)

numero_de_discos = 5
print(f"Resolvendo Torres de Hanói para {numero_de_discos} discos:")

# A primeira chamada que inicia todo o processo recursivo
# As hastes são nomeadas A (Origem), C (Destino) e B (Auxiliar)

torres_de_hanoi(numero_de_discos, 'A', 'C', 'B')