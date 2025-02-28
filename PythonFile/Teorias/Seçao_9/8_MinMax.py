"""

MIN e MAX:
    - Pode ser utilizado em listas, tuplas, dicionarios, conjuntos, etc.

    1. Utilizando min e max com números
        [1] Com definidos
        [2] Com variáveis


    2. Utilizando min e max com strings
        - Segue o formato do alfabeto, então 'a' é o menor e 'z' o maior
            - Se tiver espaços ' ' ele será menor que o 'a'.


    3. Utilizando min e max em dicionários
        - Utilizamos o argumento key.
"""

#1 UTILIZANDO MIN E MAX COM NUMEROS:

"""
# Com números definidos [1]:
numeros = [1, 3, 5, 6, 8]
print(max(numeros)) # resulta em 8
print(min(numeros)) # resulta em 1

# Com variáveis [2]:
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print(max(num1, num2))
print(min(num1, num2))
"""

#2 UTILIZANDO MIN E MAX COM STRINGS:
"""
print(max('magaiver nelson')) # resulta no v
print(min('magaiver nelson')) # resulta no espaço
print(min('magaivernelson')) # resulta no a
"""

#3 UTILIZANDO MIN E MAX COM DICIONARIOS:
"""
musicas = [
    {'titulo': 'Lua Cheia', 'tocou': 12},
    {'titulo': 'Segredos', 'tocou': 8},
    {'titulo': 'Quando o sol se for', 'tocou': 8},
    {'titulo': 'Olhos certos', 'tocou': 7},
    {'titulo': 'Outro lugar', 'tocou': 6}
]

print(max(musicas, key=lambda musica: musica['tocou'])) # Retorna o valor da lista em questão
print(max(musicas, key=lambda musica: musica['tocou']).get('titulo')) # Retorna apenas o nome da música
print(max(musicas, key=lambda musica: musica['tocou'])['titulo']) # Retorna apenas o nome da música
print(min(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']).get('titulo'))
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
"""