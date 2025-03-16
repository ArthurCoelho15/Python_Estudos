"""

TUPLAS (tuple):
    - Bastante parecida com as listas;
    - As tuplas são imutáveis, ao criar uma tupla ela não muda;
        - Deixa o código mais seguro.
    - Toda operação realizada em uma tupla cria uma nova tupla;
    - Representadas por '()' parenteses.
    - Métodos para adição e remoção de elementos não existem nas tuplas, devido as tuplas serem imutáveis.
        - Não existe append, pop, extend, etc.
    - A tupla é mais rápida do que a lista, preferível para um grande volume de dados.

    1. Tipos de tuplas:
        Funciona de modo igual as listas, podemos fazer inteiro, float, string, misturado, etc.


    2. Sintaxe das tuplas:
        Pela representação temos a tupla com (), mas a definição trata tupla o que vem acompanhada de ',' vírgula.
        [1] tupla1 = (1, 2, 3, 4)
        [2] tupla2 = 1, 2, 3 , 4
        [3] tupla3 = (1, 2, 3, 4,)
        [4] tupla4 = 1, 2, 3, 4,

        OBS: Caso especial (tupla de 1 elemento)
            tupla_Única1 = 4, -> Certo, vírgula no final
            tupla_Única2 = (4,) -> Certo, vírgula no final
            tupla_Única3 = 4 -> errado, entende como inteiro
            tupla_Única4 = (4) -> errado, entende como inteiro

        3. Desempacotamento de tuplas:
            - Podemos atribuir variáveis a valores de uma tupla.
            - Eu tenho que desempacotar a mesma quantidade de valores e variáveis.
                Não é possível desempacotar 3 variáveis em uma tupla de 4 itens.

        4. Realizando operações em uma tupla:
            Exceto o Tamanho da lista [4] todos esses tem que ser com valores inteiros ou reais.
                [1] Soma
                [2] Valor máximo
                [3] Valor mínimo
                [4] Tamanho da tupla

        5. Concatenando tuplas:
            [1] As tuplas são imutáveis, então para fazermos a concatenação outra tupla é criada.
            [2] Podemos sobrescrever os valores de uma tupla.

        6. Copiando listas:
            - Na tupla não temos a função copy() para fazer o Deep Copy igual conhecemos nas listas.
            [1] Utilizando atribuição de variável -> Na tupla não existe Shallow Copy, o valor não é alterado, portanto o 'Shallow Copy' da tupla é o 'Deep Copy' da lista.
                Nesse método fazemos a cópia de uma tupla atribuindo uma outra, ambas são independentes, uma alteração na tupla copiada não altera a tupla base.
"""


#1 TIPOS DE TUPLAS:

"""
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
"""

#2 SINTAXE DAS TUPLAS - Teórico:


#3 DESEMPACOTAMENTO DE TUPLAS:

"""
tupla_emp = ('Arthur', 'Nelso')
nome, sobrenome = tupla_emp

print(nome)
print(sobrenome)
"""


#4 OPERAÇÕES EM UMA TUPLA:

"""
tupla_op = (10, 11, 14, 20, 40)
print(tupla_op)

# Operações [1] - Soma
print(sum(tupla_op))
# Operações [2] - Valor máximo
print(max(tupla_op))
# Operações [3] - Valor mínimo
print(min(tupla_op))
# Operações [4] - Tamanho da tupla
print(len(tupla_op))
"""


#5 CONCATENAÇÃO DE TUPLAS:

"""
tupla_conc1 = (10, 11, 14, 20, 40)
tupla_conc2 = (8, 13, 16, 21, 42)

print(tupla_conc1)
print(tupla_conc2)

# Concatenando em uma nova tupla - São métodos iguais [1]
print(tupla_conc1 + tupla_conc2)

tupla_conc3 = tupla_conc1 + tupla_conc2
print(tupla_conc3)

# Sobrescrevendo uma tupla [2]
tupla_conc1 = tupla_conc1 + tupla_conc2
print(tupla_conc1)
"""


#6 COPIANDO TUPLAS:

"""
# Atribuindo variável [1] - Deep Copy
tupla_base1 = ('copiar1', 'copiar2', 'copiar3')
tupla_base2 = ('copiar4', 'copiar5', 'copiar6')

tupla_copiada1 = tupla_base1
"""