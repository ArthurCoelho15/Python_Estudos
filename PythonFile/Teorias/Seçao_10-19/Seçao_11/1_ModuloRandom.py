"""

MÓDULOS:
    - Em Python, módulos são nada mais que outros arquivos Python.

    1. Importando módulos:
        [1] Importando o módulo todo - Menos recomendado
            import nome_do_modulo
                - Utilizamos quando não sabemos exatamente que funções iremos utilizar
                    - Carrega as funções, classes, variáveis, etc.
        [2] Importando uma função específica do módulo - Mais recomendado
            from nome_do_modulo import nome_da_função

MÓDULO RANDOM:
    - Possui várias funções para geração de números pseudo-aleatórios.

    1. Funções do Random:
        [1] Random
            - Gera um número real pseudo-aleatorio entre 0 e 1.
                random.random()
        [2] Uniform
            - Gera um número real pseudo-aleatorio entre o intervalo definido
                random.uniform(num_inicial, num_final) -> Não pega o número final
        [3] Randint:
            - Gera um número inteiro pseudo-aleatorio entre o intervalo definido
                random.randint(num_inicial, num_final) -> Não pega o número final
        [4] Choice:
            - Mostra um valor aleatório entre um iterável
                - Listas, tuplas, dicionarios, strings
                choice(iteravel)
        [5] Shuffle:
            - Tem a função de embaralhar dados
                interavel = [] # exemplo para uma lista
                shuffle(iteravel)
                print(iteravel)
"""

#1 MODULO RANDOM

import random
from random import shuffle, choice


# Funções do random [1] - Random
num1 = random.random() # numero real pseudo-aleatório entre 0 e 1
print(f'num1 = {num1}')

# Funções do random [2] - uniform
num2 = random.uniform(1, 11) # numero real pseudo-aleatório entre 1 e 10
print(f'num2 = {num2}')

# Funções do random [3] - randint
num3 = random.randint(1, 11) # numero inteiro pseudo-aleatório entre 1 e 10
print(f'num3 = {num3}')

# Funções do random [4] - choice
lista_random1 = ['arthur', 'lucas', 'guilherme', 'alan']
print(f'O nome escolhido foi {choice(lista_random1)}') # Escolhe um nome de forma pseudo-aleatória da lista

# Funções do random [5] - shuffle
lista_random2 = ['arthur', 'lucas', 'guilherme', 'alan']
shuffle(lista_random2) # Embaralha de forma pseudo-aleatoria a lista
print(f'A lista foi embaralhada: \n{lista_random2}')