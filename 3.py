# 3
def adivinhar_numero(inicio, fim):
    palpite = inicio + (fim - inicio) // 2

    acertei = int(input(f"{palpite}! Acertei? (1 - sim, 2 - maior, 3 - menor): "))

    if acertei == 1:
        print("Ótimo! Acertei!")
        return
    elif acertei == 2:
        adivinhar_numero(palpite + 1, fim)
    elif acertei == 3:
        adivinhar_numero(inicio, palpite - 1)
    else:
        print("Resposta inválida. Tente novamente.")
        adivinhar_numero(inicio, fim)

adivinhar_numero(50, 100)
