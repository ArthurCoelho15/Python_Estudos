"""

Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.

"""

num = 3

for multiplo in range(1,6):
    questao = num * multiplo
    print(f'índice: {multiplo}, valor: {questao}')
