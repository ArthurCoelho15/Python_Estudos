"""

Faça uma função utilizando lambda para ordenar pelo sobrenome os nomes das pessoas em uma lista.

"""

nomes = ['Arthur C. Nelson', 'Guilherme J. C. Curso', 'Lucas Biras', 'Alan A. Aline', 'Guilherme Stif', 'Rafael Bombado']

print(nomes)

nomes.sort(key = lambda sobrenome: sobrenome.split(' ')[-1].lower())
"""
usa-se bastante a função lambda como key, aqui estamos transformando cada nome em listas ['Arthur', 'Nelson'] pelo delimitador 'espaço',
pegando o sobrenome pelo [-1], último elemento da lista e tranformando tudo em lower para normalizar a palavra na hora da classificação.
"""
print(nomes)