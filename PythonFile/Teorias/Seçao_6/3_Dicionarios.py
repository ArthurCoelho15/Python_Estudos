"""

DICIONÁRIOS / MAPAS (dict):
    - Os dicionários são coleções do tipo chave/valor.
    - Os dicionários são representados por '{}' chaves.
    - Podemos utilizar qualquer tipo de dado, inclusive lista, tupla, outros dicionários.
    - As tuplas são interessantes para serem utilizadas como chaves de dicionários, por serem imutáveis.


    1. Tipos:
        [1] Mais comum:
            paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}
        [2] Menos comum:
            paises = dict(BR = 'Brasil', EUA = 'Estados Unidos', PY = 'Paraguai')
        - Recomenda-se utilizar o tipo [1] Mais comum devido a demostrar facilmente qual o tipo de dado a user utilizado.


    2. Sintaxe:
        [1] Chave e valor são separados por dois pontos;
            chave: valor
        [2] Tanto a chave quanto o valor pode ser de qualquer tipo de dado


    3. Acessando dicionários:
        - Os dicionários não são indexados, portanto não utilizamos os índices.
         [1] Podemos acessar os dicionários via função get - Mais recomendado.
            - Essa forma é mais recomendada pois se procurarmos um valor que não existe no dicionário receberemos o None e não o KeyError
                - É mais fácil compreender que o valor não existe do que ver se o código tem realmente algum erro.
                (1) dicionario.get(var)
                (2) dicionario.get(var, var_consequencia)
                    - Esse 'var_consequencia' botamos caso não encontre a chave buscada no 'var'.
         [2] Podemos acessar os dicionários pela chave.


    4. Podemos verificar se determinada chave está presente no dicionário
        - Pesquisamos pela chave, não pelo valor.


    5. Algumas funções que poderemos utilizar:
        [1] Adicionar/Atualizar:
            - Adicionar e atualizar funciona exatamente da mesma forma
                - Adicionar: poe uma chave que ainda não existe;
                - Atualizar: poe uma chave que já existe e muda o valor.
            (1) atribuir a chave e valor do dicionário - Mais comum
            (2) update() -> dicionario.update()
        [2] Remover:
            (1) Função pop - Mais comum
                - Remove um elemento do dicionário com base na chave
                    pop() -> dicionario.pop(chave)
            (2) Função del
                - Mesma coisa do pop
                    del dicionario[chave]
        [3] Método não usual de criação de dicionários:
            (1) Função Fromkeys
                - Vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.
                    dicionario = {}.fromkeys(var_iterável, valor)
        [4] Descobrindo todas as chaves do dicionário:
            (1) Função Keys
                keys() -> dicionario.keys()
        [5] Descobrindo todos os valores do dicionário:
            (1) Função values
                values() -> dicionario.values()
        [6] Tuplas para descobrir as chaves e valores juntos do dicionário:
            (1) Função items
                items() -> dicionario.items()

    6. Copiando dicionários:
        - Da mesma forma que as listas
            - Deep Copy: Função copy()
            - Shallow copy: Atribuindo o mesmo valor de variável.


    7. Iterando sobre dicionários:
        [1] Utilizando o for


    8. Desempacotamento de dicionários:
        - Podemos atribuir variáveis a valores de uma lista.
        - Eu tenho que desempacotar a mesma quantidade de valores e variáveis.
            - Não é possível desempacotar 3 variáveis em uma lista de 4 itens.

    9. Realizando operações em uma lista:
        Exceto o Tamanho da lista [4] todos esses tem que ser com valores inteiros ou reais.
            [1] Soma
            [2] Valor máximo
            [3] Valor mínimo
            [4] Tamanho da lista
"""


#1 TIPOS - Teórico:


#2 SINTAXE:

"""
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}
print(paises)
"""


#3 ACESSANDO DICIONÁRIOS:

"""
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

# Função get [1]:
print(paises.get('BR'))
    # print(paises.get('PE')) -> None, PE não existe no dicionário.
print(paises.get('PR', 'Não encontrado'))

# Acessando pela chave [2]:
print(paises['BR'])
    # print(paises['PE']) -> KeyError, PE não existe no dicionário.
"""


#4 VERIFICANDO A PRESENÇA:

"""
animais = {'dog': 'Cachorro', 'cat': 'Gato', 'mouse': 'Rato'}

print('cat' in animais)
print('bird' in animais)
"""


#5 FUNÇÕES:

"""
salario = {'janeiro': 1000, 'fevereiro': 900}

print(salario)

# Adicionando/Atualizando [1] - Atribuindo chave e valor (1):
salario['março'] = 1100
print(salario)
salario['janeiro'] = 2000
# Adicionando/Atualizando [1] - Função update (2):
salario_abril = {'abril': 1300}
salario.update(salario_abril)
print(salario)
salario.update({'maio': 1500})
print(salario)
# Removendo [2]:
salario.pop('maio')
print(salario)
# Criação Nada usual [3]:
criar1 = {}.fromkeys('a', 1)
print(criar1)
criar2 = {}.fromkeys(['nome', 'cpf', 'email', 'idade'], 'desconhecido')
print(criar2)
criar3 = {}.fromkeys('teste', 'resultado')
print(criar3)
criar4 = {}.fromkeys(range(1, 11), 'novo_valor')
print(criar4)
# Descobrindo as chaves do dicionário [4]
print(salario.keys())
# Descobrindo os valores do dicionário [5]
print(salario.values())
# Descobrindo as chaves e valores associados [6]
print(salario.items())
"""


#7 ITERANDO SOBRE DICIONÁRIOS:

# Iterando com for [1]

"""
salario = {'janeiro': 1000, 'fevereiro': 900, 'março': 1150, 'abril': 1300}

print(salario)

for chave in salario: # Nao recomenda-se usar essa
    print(chave)

for chave in salario: # Nao recomenda-se usar esse
    print(salario[chave])

for chave in salario:
    print(f'Em {chave} recebi R$ {salario[chave]},00.')

for chave in salario.keys(): # Recomenda-se usar essa, modo pythonico
    print(salario[chave])

for valor in salario.values(): # Recomenda-se usar esse, modo pythonico
    print(valor)
    
for chave, valor in salario.items():
    print(f'Chave = {chave} e Valor = {valor}')
"""


#8 Operações:

"""
salario = {'janeiro': 1000, 'fevereiro': 900, 'março': 1150, 'abril': 1300}

# Operações [1] - Soma
print(sum(salario.values()))
# Operações [2] - Valor máximo
print(max(salario.values()))
# Operações [3] - Valor mínimo
print(min(salario.values()))
# Operações [4] - Tamanho da lista
print(len(salario))
"""
