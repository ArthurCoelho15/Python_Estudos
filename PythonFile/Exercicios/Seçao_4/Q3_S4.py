"""

Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

"""

numero = int(input("Digite um numero inteiro: "))
"""
if numero % 2 == 0:
    print(f'O numero {numero} é par!')
else:
    print(f'O numero {numero} é impar!')
"""
def tipo(numero):
    if numero % 2 == 0:
        print(f"o numero {numero} é par")
    print(f"o numero {numero} é impar")

tipo(numero)