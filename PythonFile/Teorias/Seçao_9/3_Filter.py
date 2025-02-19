"""

FILTER:
    - Serve para filtrar dados de uma determinada coleção
    - Após utilizar a função filter() depois da primeira utilização o resultado zera, apaga da memória.
    - Biblioteca para trabalhar com dados estatísticos: statistics

    1. Sintaxe:
        - A função recebe dois parâmetros, sendo o primeiro uma função e o segundo um iterável.
            - filter() -> filter(função, iterável)

    2. Realizando operações:
        [1] Utilizando biblioteca para média;
        [2] Filtrando dados de uma lista;
        [3] Filtrando dados de um dicionário.

    3. Trabalhando com filter e map
"""

#2 REALIZANDO OPERAÇÕES

"""
# UTILIZANDO BIBLIOTECA PARA MÉDIA [1]:

import statistics

dados = [1.2, 2.6, 0.8, 2.5, 3.5, 4.5, 0.2, 1.3]
print(dados)

media = statistics.mean(dados)
print(media)

filtro = filter(lambda x: x > media, dados)
print(list(filtro))

"""

"""
# FILTRANDO DADOS DE UMA LISTA [2]:

paises = ['', 'Argentina', 'Brasil', '', 'França', '', 'Portugal']

# Tipo 1:
filtro1 = filter(lambda x: x != '', paises)
print(list(filtro1))
# Tipo 2:
filtro2 = filter(None, paises)
print(list(filtro2))
"""

"""
# FILTRANDO DADOS DE UM DICIONÁRIO [3]:

usuarios = [
        {"username": "arthur", "tweets": ["Bom dia"]},
        {"username": "lucas", "tweets": ["Boa tarde", "one piece"]},
        {"username": "guilherme", "tweets": []},
        {"username": "alan", "tweets": []},
]

# Forma 1:
inativos1 = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
print(inativos1)
# Forma 2:
inativos2 = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos2)
"""


#3 TRABALHANDO COM FILTER E MAP

"""
instrutores = ['Arthur', 'Lucas', 'Alan', 'Guilherme']

lista_inst = list(map(lambda nome: f'Seu instrutor é {nome}', filter(lambda nome2: len(nome2) > 6, instrutores)))
print(lista_inst)
"""