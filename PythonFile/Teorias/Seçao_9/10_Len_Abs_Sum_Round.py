"""

1. LEN:
    - Retorna o tamanho de um iterável

2. ABS:
    - Retorna o valor absoluto de um número, ou seja, o módulo
    - Trabalha nos números inteiros ou reais.

3. Sum:
    - Retorna a soma de um conjunto de números.

    [1] Sintaxe:
        Sum() -> sum(parametro, valor_inicial)

4. Round:
    - Arredonda um número

    [1] Sintaxe:
        Round() -> round(parametro, casas_pos_virgula)
            - Se a precisão nao for informada, retorna o inteiro mais próximo
                - 1 até 1.5 vira 1; 1.6 até 2 vira 2.
"""

#1 LEN:
"""
print(len('Magaiver Nelson'))
print(len([1, 2, 3, 4]))
print(len((1, 2, 3, 4)))
print(len({1, 2, 3, 4}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
print(len(range(0, 10)))
"""

#2 ABS:
"""
print(abs(5))
print(abs(-5))
print(abs(3.76))
"""

#3 SUM:

"""
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
set = {1, 2, 3, 4, 5}
dicio = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}

print(sum(lista))
print(sum(lista, 5)) # Soma os valores com a condição inicial 5, ou seja, sum(lista) + 5

print(sum(dicio)) # Gera erro pois tenta somar as chaves
print(sum(dicio.values())) # Resulta na soma dos valores
"""

#4 ROUND:

print(round(1.4))
print(round(10.5))
print(round(1.6))

print(round(10.83217, 1))
print(round(10.83217, 2))
print(round(10.83217, 3))

