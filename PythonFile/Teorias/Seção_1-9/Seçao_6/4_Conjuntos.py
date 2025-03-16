"""

CONJUNTOS (Sets):
    - Em qualquer linguagem de programação, quando falamos de conjuntos estamos fazendo referência à Teoria dos Conjuntos da matemática.
    - Os Sets são representados por '{}' Chaves;
        - Um dicionário tem chave e valor, os Sets tem apenas o valor.
    - Os Sets não possuem valores duplicados;
    - Os Sets não possuem valores ordenados;
    - Os Sets não são acessados via índice, ou seja, não são indexados.
    - Os Sets são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordem. Não precisamos nos preocupar com chaves, valores e itens duplicados.


    1. Tipos:
        - Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro e não fará parte do conjunto.
        [1] Forma 1: Mais comum
            var = {valor1, valor2, valor3, valor4, etc...}
        [2] Forma 2:
            var = set({valor1, valor2, valor3, valor4, etc...})


    2. Algumas funções que poderemos utilizar nos conjuntos:
        [1] Adicionando elementos:
            add() -> conjunto.add()
        [2] Removendo elementos:
            (1) Função remove:
                - Se o valor não existir, vai rolar um KeyError.
                    remove() -> conjunto.remove(valor)
            (2) Função discard:
                - Se o valor não existir não vai gerar error.
                    discard() -> conjunto.discard(valor)
            (3) Clear:
                - Remove TODOS os elementos do conjunto.
                    clear() -> conjunto.clear(), depois printa.


    3. Métodos matemáticos dos conjuntos:
        [1] União:
            - Criar um conjunto a partir de outros, unido-os, não repete valores.
                (1) Função Union - Mais recomendado devido a visualização:
                    - A ordem de escrita não importa.
                        Union() -> var = conjunto1.union(conjunto2)
                (2) Caractere '|' Pipe:
                    - A ordem da escrita não importa.
                        var = conjunto1 | conjunto2
        [2] Interseção:
            - Criar um conjunto a partir de outros, pegando apenas os valores presentes em ambos.
                (1) Função intersection:
                    - A ordem da escrita não importa.
                        var = conjunto1.intersection(conjunto2)
                (2) Caractere '&' e comercial:
                    - A ordem da escrita não importa.
                        var = conjunto1 & conjunto2
        [3] Diferença entre conjuntos:
            - Cria um conjunto a partir de outros, pegando apenas os valores que estão presentes em um e não em outro.
                (1) Função difference:
                    - A ordem da escrita importa, vai avaliar o 1º conjunto e verificar a diferença do 2º.
                        difference() -> var = conjunto1.difference(conjunto2)


    4. Realizando operações em um conjunto:
        - Exceto o Tamanho da lista [4] todos esses tem que ser com valores inteiros ou reais.
            [1] Soma
            [2] Valor máximo
            [3] Valor mínimo
            [4] Tamanho da lista
"""

#1 TIPOS:

"""
# Forma 1 [1] - Mais comum:
s1 = {1, 'a', True, 7.5}
print(s1)
# Forma 2 [2]:
s2 = set({2, 'b', False, 5.7})
print(s2)
"""


#2 FUNÇÕES:

"""
# Adicionando elementos [1]:
s3 = {1, 2 , 3}
print(s3)
s3.add(4)
s3.add(4) # Duplicidade não gera erro, apenas é ignorado e não adicionado
print(s3)

# Removendo elementos num conjunto [2]:
s4 = {1, 2, 3, 4, 5, 6}
print(s4)
s4.remove(3) # Aqui dizemos qual elemento será removido, não tratamos de índice em conjuntos.
print(s4)
s4.discard(1) # Aqui dizemos qual elemento será removido, não tratamos de índice em conjuntos.
print(s4)
s4.clear()
print(s4)
"""

#3 MÉTODOS MATEMÁTICOS DOS CONJUNTOS:


estudantes_python = {'arthur', 'nelson', 'alan', 'afonso', 'lucas'}
estudantes_java = {'lucas', 'marcos', 'pedro', 'afonso'}

# União [1]:
print(f'Estudantes python: {estudantes_python}')
print(f'Estudantes java: {estudantes_java}')

    # União [1] - Função Union (1):
Uniao_programacao1 = estudantes_python.union(estudantes_java)
print(Uniao_programacao1)
    # União [2] - Caractere Pipe (2):
Uniao_programacao2 = estudantes_python | estudantes_java
print(Uniao_programacao2)

# Interseção [2]:

    # Interseção [2] - Função intersection (1):
Intersecao1 = estudantes_python.intersection(estudantes_java)
print(Intersecao1)
    # Interseção [2] - Caractere & (2):
Intersecao2 = estudantes_python & estudantes_java
print(Intersecao2)

# Diferença entre conjuntos [3]:

# Função Difference (1):
dif1 = estudantes_python.difference(estudantes_java)
print(dif1)
dif2 = estudantes_java.difference(estudantes_python)
print(dif2)


#6 REALIZANDO OPERAÇÕES


Conjunto_Operacoes = {1, 2, 3, 4, 5, 7.6}

# Operações [1] - Soma
print(sum(Conjunto_Operacoes))
# Operações [2] - Valor máximo
print(max(Conjunto_Operacoes))
# Operações [3] - Valor mínimo
print(min(Conjunto_Operacoes))
# Operações [4] - Tamanho da lista
print(len(Conjunto_Operacoes))
