# 4
def multiplicar_recursivo(a, b):
    if b == 0:
        return 0
    
    return a + multiplicar_recursivo(a, b - 1)

numero1 = 5
numero2 = 3
resultado = multiplicar_recursivo(numero1, numero2)

print(resultado)