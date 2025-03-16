"""

SORTED:
    - Diferentemente da função 'Sort', o SORTED pode ser utilizado em qualquer iterável.
        - Sort só pode ser utilizado em listas.
    - Não afeta a lista base, diferentemente do 'Sort'.
    - Sempre vai gerar uma nova lista.

    1. Sintaxe:
        [1] Sorted normal:
            - Sorted() -> Sorted(parametro)
        [2] Sorted com parametro reverse:
            - Sorted() -> Sorted(parametro, reverse=bool)
        [3] Sorted com parametro key:
            - Sorted() -> Sorted(parametro, key=ordenar_por_qual_chave)
            - Utilizada para fazer o sorted em dicionarios

    2. Iterando em dicionários com sorted
"""

#1 SINTAXE:

"""
# Sorted normal [1]:

numeros = [6, 8, 2, 3]

print(numeros)
print(sorted(numeros)) # Ordena em ordem crescente

print(numeros) # O sorted não afetou a lista numeros
"""
"""
# Sorted com parametro reverse [2]:

print(sorted(numeros, reverse=True)) # Ordena em ordem decrescente
"""

# Sorted em dicionarios [3]

paises = [{'nome': 'Brasil', 'sigla': 'BR', 'populacao': '290milhoes', 'estados': 26},
          {'nome': 'Estados Unidos', 'sigla': 'EUA'},
          {'nome': 'Argentina', 'sigla': 'AR', 'populacao': '80milhoes'}
          ]

#print(sorted(paises, key=len))
#print(sorted(paises, key=len, reverse=True))

musica = [
    {'titulo': 'Lua Cheia', 'tocou': 12},
    {'titulo': 'Segredos', 'tocou': 8},
    {'titulo': 'Quando o sol se for', 'tocou': 8},
    {'titulo': 'Olhos certos', 'tocou': 7},
    {'titulo': 'Outro lugar', 'tocou': 6}
]

# Ordenando da menos tocada para a mais tocada:
print(sorted(musica, key=lambda musica: musica['tocou']))

# Ordenando da mais tocada para a menos tocada:
print(sorted(musica, key=lambda musica: musica['tocou'], reverse=True))


#2 ITERANDO EM DICIONÁRIOS COM SORTED:

musicas = sorted(musica, key=lambda musica: musica['tocou'], reverse=True)
for i in range(len(musicas)):
    print(f'TOP {i+1}: {musicas[i].get('titulo')}, com {musicas[i].get('tocou')} vezes tocadas')
