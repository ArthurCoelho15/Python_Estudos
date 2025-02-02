"""

Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

"""

import math

numero1 = int(input('digite o primeiro inteiro: '))
numero2 = int(input('digite o segundo numero inteiro: '))
numero3 = int(input('digite o terceiro numero inteiro: '))

soma_quad = pow(numero1, 2) + pow(numero2, 2) + pow(numero3, 2)

print(f'A soma dos numeros e: {soma_quad}')