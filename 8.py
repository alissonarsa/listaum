def inverter_string_dinamico(palavra):
    lista_resultado = []
    
    _inverter_recursivo(palavra, lista_resultado)
    
    return "".join(lista_resultado)


def _inverter_recursivo(palavra, lista_resultado):
    if not palavra:
        return

    ultima_letra = palavra[-1]
    
    lista_resultado.append(ultima_letra)
    
    _inverter_recursivo(palavra[:-1], lista_resultado)


minha_palavra = "Alisson"
palavra_invertida = inverter_string_dinamico(minha_palavra)

print(minha_palavra)
print(palavra_invertida)