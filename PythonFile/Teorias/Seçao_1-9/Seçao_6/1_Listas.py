"""

LISTAS (list):
    - As listas funcionam como matrizes/vetores/arrays em outras linguagens, com a diferença de serem dinâmicas e poderemos inserir qualquer tipo de dados.
    - Representadas por '[]' colchetes

    # Linguagens C/Java: Arrays
        - Possuem tamanho e tipo de dado fixo
            Se criarmos um array do tipo int e com tamanho 5, esse array SEMPRE será do tipo inteiro e terá no MAXIMO 5 valores.

    1. Em Python: Listas
        - Possuem tamanho e tipo de dado dinâmico
            Podemos simplesmente criar a lista e ir adicionando elementos, podemos adicionar QUALQUER tipo de dado
        - As listas em Python são representadas por colchetes [].
        - Tipos de listas:
            [1] Podemos criar listas de números;
            [2] Podemos criar listas de strings;
            [3] Podemos criar listas vazias (para ir adicionando algo);
            [4] Podemos criar listas de range;
            [5] Podemos criar listas a partir de strings, fazendo cast;
            [6] Podemos misturar tipos de dados em uma lista.


    2. Algumas funções que poderemos utilizar nas listas:
        [1] Ordenar a lista:
            sort() -> lista.sort(), depois printa
        [2] Contar a ocorrência de um valor:
            count() -> print(lista.count(valor))
        [3] Adicionar elementos:
            - Só conseguiremos adicionar um elemento por vez (append)
                -Quando adicionamos vai pro final da lista
                    append() -> lista.append(valor), depois printa
            - Podemos botar vários elementos de uma vez (extend)
                -Não aceita valor único, só aceita Lista, string, etc, valor unico é append!
                - Quando adicionamos vai pro final da lista
                    extend() -> lista.extend([valor1, valor2, valor3, etc]), depois printa
            - Podemos adicionar elementos escolhendo o índice onde ele vai ficar (insert)
                - s
                    insert() -> lista.insert(posicao, valor)
        [4] Inverter a lista:
            - Quando quisermos inverter a posicao dos valores da lista
                reverse() -> lista.reverse(), depois printa
                print(lista1[::-1])
        [5] Copiar uma lista:
            - Quando quisermos copiar uma lista
                copy() -> lista1 = lista0.copy, depois printa
        [6] Saber o tamanho de uma lista:
            - Quando quisermos saber a quantidade de elementos de uma lista
                len() -> print(len(lista))
        [7] Remover o elemento de uma lista:
            - Podemos remover o último elemento de uma lista, ou pelo indice
                pop() -> lista.pop(), depois printa
                pop(indice) -> lista.pop(indice), depois printa
        [8] Remover todos os elementos da lista:
            - Podemos remover todos os elementos de uma lista
               clear() -> lista.clear(), depois printa
        [9] Transformando lista em string:
            - Na Seção 3 fizemos o cast de string para lista, podemos fazer o inverso agora
                join() -> var = 'delimitador'.join(), depois printa

    3. Utilizando listas com outros interativos:
        [1] While
        [2] For
        [3] Variáveis em listas
        [4] Gerar indices num For
        [5] Descobrir o índice de um valor da lista
            - index() -> lista.index(valor) ou lista.index(valor, range_inicial, range_final)
            - Retorna o índice do primeiro item encontrado (caso tenha repetição do item na lista)

    4. Revisão de slicing:
        [1] inicio
            lista[x::]
        [2] fim
            lista[:x:]
        [3] passo
            lista[::x]
            - Se tivermos numeros ordenados pode ser bom para avaliarmos apenas os pares ou ímpares.

    5. Trocando valores de uma lista:
        [1] trocando valores - Metodo 1
        [2] trocando valores - Metodo 2

    6. Realizando operações em uma lista:
        - Exceto o Tamanho da lista [4] todos esses tem que ser com valores inteiros ou reais.
            [1] Soma
            [2] Valor máximo
            [3] Valor mínimo
            [4] Tamanho da lista

    7. Desempacotamento de lista:
        - Podemos atribuir variáveis a valores de uma lista.
        - Eu tenho que desempacotar a mesma quantidade de valores e variáveis.
            Não é possível desempacotar 3 variáveis em uma lista de 4 itens.

    8. Copiando listas:
        [1] Utilizando a função Copy() -> Chamado de Deep Copy
            Nesse método fazemos a cópia de uma lista para outra, ambas são independentes, uma alteração na lista copiada não altera a lista base.
            Copy() -> lista.copy()
        [2] Utilizando atribuição de variável -> Chamado de Shallow Copy
            Nesse método fazemos a cópia de uma lista atribuindo uma outra, as listas são dependentes uma da outra, uma alteração em uma afeta a outra.
"""


#1 TIPOS DE LISTAS

"""
# Tipo de lista [1]
lista1 = [1, 5, 5, 23, 219, 2391, 932]
# Tipo de lista [2]
lista2 = ['A', 'r', 't', 'h', 'u', 'r', ' ', 'N', 'e', 'l', 's', 'o', 'n']
# Tipo de lista [3]
lista3 = []
# Tipo de lista [4]
lista4 = list(range(11))
# Tipo de lista [5]
lista5 = list('Guilherme Jenipapo')
# Tipo de lista [6]
lista6 = [1, 32.4, True, 'Nelson', [3, 2 ,4]]

num = '23'
if num in lista1:
    print(f'Encontrei o {num}')
else:
    print(f'Não encontrei o {num}')
"""

#2 FUNÇÕES

"""
# Função ordenar [1]
lista1.sort()
print(lista1)

# Função contagem de valores [2]
print(lista1.count(5))
print(lista5.count('e'))

# Função adicionar valor [3]
print(lista1)
lista1.append(6)

print(lista1)

lista3.append([999, 998, 997])
print(lista3)

lista3.extend([100, 101, 102])
print(lista3)

lista3.insert(2, 'posicao')
print(lista3)

# Função reverse [4]
lista5.reverse()
print(lista5)

# Função copy [5]
lista0 = lista1.copy()
print(lista0)

# Função len [6]
print(len(lista0))

# Função remover [7]
lista0.pop()
print(lista0)
lista0.pop(1)
print(lista0)

# Função clear [8]
listacls = list(range(10))
print(listacls)
listacls.clear()
print(listacls)

# Função join [9]
joina = 'Teste do join'
print(joina.split())
join_splitado = ['Teste', 'do', 'join']
join_joinado = ' '.join(join_splitado)
print(join_joinado)
"""

#3 ITERATIVOS

"""
# Iterativo [1]
carrinho = []
produto = ''

while produto != 'sair':
    produto = input("Adicione um produto na lista ou digite 'sair' para sair: ")
    if produto != 'sair':
        carrinho.append(produto)
print(carrinho)

# Iterativo [2]
for produto in carrinho:
    print(produto)

# Iterativo [3]
num1 = 1
num2 = 2
num3 = 3

numeros = [num1, num2, num3]
print(numeros)

# Iterativo [4]
cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)

# Iterativo [5]
print(cores.index('amarelo'))
"""

#4 REVISÃO DE SLICING

"""
listaslc = [1, 2, 3, 4, 5, 6]

# Slicing [1]
print(listaslc[2::]) # começa do indice 2 até o final, passo = 1 (padrão)

# Slicing [2]
print(listaslc[:4:]) # Começa do indice 0 até o indice 4, passo = 1 (padrão)

# Slicing [3]
print(listaslc[::2]) # Pega printa a lista toda sendo que a cada 2 indices
"""

#5 TROCANDO VALORES

"""
troca = ['Valor1', 'Valor2']
troca2 = ['Valor3', 'Valor4']

# Trocando valores [1]
print(troca)
troca[0], troca[1] = troca[1], troca[0]
print(troca)

#  Trocando valores [2]
print(troca2)
troca2.reverse()
print(troca2)
"""

#6 REALIZANDO OPERAÇÕES

"""
Lista_Operacoes = [1, 2, 3, 4, 5, 7.6]

# Operações [1] - Soma
print(sum(Lista_Operacoes))
# Operações [2] - Valor máximo
print(max(Lista_Operacoes))
# Operações [3] - Valor mínimo
print(min(Lista_Operacoes))
# Operações [4] - Tamanho da lista
print(len(Lista_Operacoes))
"""

#7 DESEMPACOTAMENTO DE LISTAS

"""
lista_empacotada = [1, 2, 3, 4]

desem1, desem2, desem3, desem4 = lista_empacotada

print(desem1)
print(desem2)
print(desem3)
print(desem4)
"""

#8 COPIANDO LISTAS

"""
lista_base = [1, 2, 3, 4]

# Função copy [1] - Deep copy
deep = lista_base.copy()
print(lista_base)
print(deep)
deep.append(5)
print(lista_base)
print(deep)

print(" ")
# Atribuindo variável [2] - Shallow copy
shallow = lista_base
print(lista_base)
print(shallow)
shallow.append(5)
print(lista_base)
print(shallow)
"""

