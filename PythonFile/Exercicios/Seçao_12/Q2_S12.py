"""

Faça um programa que receba do usuário o nome de um arquivo txt e mostre quantas vogais e quantas consoantes existem no arquivo


"""

from collections import Counter

vogais = 'aeiou'
consoantes = ('bcdfghjklmnpqrstvwxyz')
contador = {'vog': 0, 'cons':0}

with open('C:\\Users\\arthu\\OneDrive\\Área de Trabalho\\Faculdade\\Programação\\Exercicios\\s12-exercicios\\arq.txt', 'r') as cons_vog:
    for letra in cons_vog.read():
        if letra in list(vogais):
            contador['vog'] += 1
        elif letra in list(consoantes):
            contador['cons'] += 1
        else:
            pass

print(f'No arquivo temos:\n'
      f' - Vogais: {contador['vog']}\n'
      f' - Consoantes: {contador['cons']}')
