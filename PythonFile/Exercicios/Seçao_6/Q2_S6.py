"""

Faça um programa que leia um número inteiro positivo N e imprima os números naturais de 0 até N em ordem crescente e depois em ordem decrescente.

"""

numero_N = int(input('Digite um número: '))
lista = []

# Ordem crescente:
"""
for contagem in range(0,numero_N+1):
    lista.append(contagem)

print(lista)
print(sum(lista))
"""

# Ordem decrescente:
"""
for contagem in range(numero_N,0,-1):
    lista.append(contagem)

print(lista)
print(sum(lista))
"""

# Ordem crescente - Par:
"""
for contagem in range(0,numero_N+1):
    if contagem % 2 == 0:
        lista.append(contagem)

print(lista)
print(sum(lista))
"""

# Ordem crescente - Impar:
"""
for contagem in range(0,numero_N+1):
    if contagem % 2 != 0:
        lista.append(contagem)

print(lista)
print(sum(lista))
"""