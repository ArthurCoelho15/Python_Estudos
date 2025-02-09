"""

Faça um programa que simula o lançamento de 2 dados N vezes, e tem como saída o número de cada dado e a relação entre eles (>, < ou =) de cada lançamento.

"""
import random

QuantidadeN = int(input("Digite a quantidade de jogadas: "))
i = 0
vitorias_dado1 = 0
vitorias_dado2 = 0
empates = 0

while i < QuantidadeN:
    dado1 = random.randrange(1,6)
    dado2 = random.randrange(1, 6)
    print(f'\nDado1 = {dado1} e Dado2 = {dado2}')

    if dado1 == dado2:
        print('Empate, dados iguais!')
    elif dado1 > dado2:
        print('Vitória do Dado1!')
        vitorias_dado1 = vitorias_dado1 + 1
    else:
        print('Vitória do Dado2!')
        vitorias_dado2 = vitorias_dado2 + 1

    ganhador = {'Dado1': vitorias_dado1, 'Dado2': vitorias_dado2}
    i = i + 1

print(ganhador)

if ganhador['Dado1'] > ganhador['Dado2']:
    print(f'\nO vencedor foi o Dado1 com {max(ganhador.values())}')
else:
    print(f'\nO vencedor foi o Dado2 com {max(ganhador.values())}')
