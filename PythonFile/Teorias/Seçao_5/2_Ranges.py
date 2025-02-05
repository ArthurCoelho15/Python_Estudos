"""

RANGES:
    Ranges são utilizados para gerar sequências númericas de maneira especificadas.
        [1] range(valor_de_parada)
            OBS: valor_de_parada não inclusive (início padrão = 0, e passo de 1 em 1)
        [2] range(valor_de_inicio, valor_de_parada)
            OBS: incrementa de 1 em 1.
        [3] range(valor_de_inicio, valor_de_parada, incremento)
        [4] range(valor_de_inicio, valor_de_parada, incremento_negativo)
            OBS: A diferença desse pro outro é que aqui da pra decrementar.

    OBS: podemos converter esse range em uma lista botando list() -> podemos usar isso para ver o range no terminal
        Ex: list(range(opcao_[1],[2],[3],[4])
"""

"""# Forma [1]
for num in range(11):
    print(num)

# Forma [2]
for num2 in range(1, 11):
    print(num2)

# Forma [3]
for num3 in range(1, 11, 2):
    print(num3)"""

# Forma [4]
for num4 in range(10, 0, -1):
    print(num4)