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