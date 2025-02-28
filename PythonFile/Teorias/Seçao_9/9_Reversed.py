"""

REVERSED:
    - Diferentemente da função 'Reverse', o REVERSED pode ser utilizado em qualquer iterável.
        - Reverse só pode ser utilizado em listas.
    - Não afeta a lista base, diferentemente do 'Reverse'.
    - Sempre vai gerar um objeto chamado List Reverse Iterator.
        - Podemos transformar em lista, tupla, dicionario ou conjunto depois.

    1. Sintaxe:
        Reversed() -> Reversed(parametro)


    2. Transformando o List Reverse Iterator em:
        [1] Lista;
        [2] Tupla;
        [3] Set.
            - Não guarda a ordenação, não tão eficaz.


    3. Iterando com reversed().
        [1] Utilizando for;
        [2] Sem utilizar for:
            - Alterando o passo no range.


    4. Alternativas para não usar o reversed():
        [1] Alterando na string;
        [2] Alterando na lista.

"""

#1 SINTAXE:

"""
lista = [1, 2, 3, 4, 5]
print(reversed(lista))
"""

#2 TRANSFORMANDO O LISTA REVERSE ITERATOR:

"""
# Transformando em lista [1]:
print(list(reversed(lista)))

# Transformando em tupla [2]:
print(tuple(reversed(lista)))

# Transformando em set [3]:
print(set(reversed(lista))) # O set não guarda a ordenação, então não é tão eficaz
"""

#3 ITERANDO COM REVERSED():

# Utilizando for [1]:
"""
for letra in reversed('Magaiver Nelson'):
    print(letra, end='')
print()

# Sem utilizar for [2]:
for n in range(9, 1, -1):
    print(n)
"""

#4 ALTERNATIVAS PARA NÃO UTILIZAR O REVERSED():
"""
# Alterando na string [1]:
print('Magaiver Nelson'[::-1])

# Alterando na lista [2]:
print(''.join(list(reversed('Magaiver Nelson'))))
"""
