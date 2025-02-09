"""

Faça um programa que faça a leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.
    - Entende-se que o número negativo não esteja na leitura do programa.
"""

lista = []

while True:
    numero = int(input("Digite um número inteiro: "))
    if numero < 0:
        break
    lista.append(numero)
    print(lista)

lista.sort()

print(lista)
print(f'O maior número da lista é: {max(lista)}')
print(f'O menor número da lista é: {min(lista)}')
