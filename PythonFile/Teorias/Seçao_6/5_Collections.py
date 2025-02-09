"""

COLLECTIONS:
    Collections -> High-performance Container Datatypes

    [1] Counters:
        Counter ->  Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
            -  O Collections Counter tem a sintaxe parecida com a do dicionário.
                - A Chave é o elemento da lista passada como parâmetro e o valor é a quantidade de ocorrências.

    [2] Default Dict:
        - O Default Dict é um caso a especial do dicionário, ao 'pesquisar' um valor inexistente no dicionário podemos inseri-lo e atribuir um valor padrão para ele.
        - Podemos utilizar o DD para evitar KeyError e estudarmos requisições do usuário.
    [3] Ordered Dict:
        - O Ordered Dict é um caso especial do dicionário, aqui obteremos o dicionário ordenado.
    [4] Named Tuple:
        - A Named Tuple é um caso especial da Tupla, aqui podemos fornecer um nome e uma quantidade ilimitada de parâmetros.
        - Uma vantagem é o modo onde conseguimos acessar os parâmetros, sem necessitar do índice.
        [1] Podemos acessar:
            (1) Pelo índice
            (2) Pelo parâmetro
"""

#1 COUNTERS:

"""
from collections import Counter

lista = [1, 1, 3, 54, 6, 2, 7, 8, 9, 0, 1, 11 ,3, 2, 5]
col = Counter(lista)

print(lista)
print(col)
print(type(col))

nome = 'Arthur Oscar Ferreira Coelho dos Santos'
print(Counter(nome).most_common(3))
"""

#2 DEFAULT DICT:

"""
from collections import defaultdict

paises = defaultdict(lambda: "Não existe")

paises['BR'] = 'Brasil'

print(paises)
print(paises['AN']) # No dicionário comum resultaria em KeyError.
print(paises)
"""

#3 ORDERED DICT:



#4 NAMED TUPLE:

from collections import namedtuple

# Tipos de sintaxe:
cachorro = namedtuple('Cachorro', 'idade raca nome') # Tipo 1
gato = namedtuple('gato', 'idade, raca, nome') # Tipo 2
macaco = namedtuple('macaco', ['idade', 'raca', 'nome']) # Tipo 3 - Preferível

tupla = macaco(idade = 10, raca = 'Madagascar', nome = 'Mason')
print(tupla)

# Tipos de acesso [1]:

# Acessando pelo índice (1):
print(tupla[0]) # Pegando a idade
print(tupla[1]) # Pegando a raça
print(tupla[2]) # Pegando o nome

# Acessando pelo parâmetro (2):
print(f'\n{tupla.idade}') # Pegando a idade
print(tupla.raca) # Pegando a raça
print(tupla.nome) # Pegando o nome

