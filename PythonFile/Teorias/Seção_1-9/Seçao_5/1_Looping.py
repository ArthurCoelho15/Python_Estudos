"""

LOOPING:
    Estrutura de repetição

    [1] For:
        for item in lista:
        // execução do looping

        # Enumerate(var) -> transforma a string em uma tupla (indice, valor)
            - se quiser descartar algum valor troca no for por '_'
            - se usar ex coletivo:
                print(coletivo[0]) -> tras só indice; print(coletivo[1]) -> tras só valor.

        OBS: por padrão o print tem várias variaveis, uma delas é o end='\n' -> o \n ta pulando uma linha no final do texto
a pira que da pra fazer é escrever o end e botar end='', que ai não pula a linha.
"""

nome = 'Arthur Coelho'

# For de forma individual [1]
"""for indice, valor in enumerate(nome):
    # for _, cachorro in enumerate(): -> descartou o indice
    print(f'{indice} é {valor}')"""
# For de forma coletiva [1]
for coletivo in enumerate(nome):
    print(coletivo[1], end="")
