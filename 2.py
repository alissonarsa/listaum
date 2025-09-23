palavra = "alisson"

# 2
def inverter_string(palavra):
    if len(palavra) <= 1:
        return palavra

    return palavra[-1] + inverter_string(palavra[0:-1])

palavrainvertida = inverter_string("alisson")
print(f"A palavra invertida é: {palavrainvertida}")