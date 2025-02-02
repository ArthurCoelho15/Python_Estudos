"""

Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.

"""
import math

numero = float(input('Digite um numero: '))

if numero >= 0:
    num_quad = pow(numero, 2)
    print(f"O numero digitado foi {numero} e seu quadrado é {num_quad}")
else:
    print('O numero digitado é inválido!')