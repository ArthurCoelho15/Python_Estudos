"""

Usando o switch, escreva um programa que leia um inteiro entra 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, [...].

"""


dia = int(input('Digite um dia da semana de 1 a 7: '))

if dia in range(1,7):
    match dia:
        case 1:
            print(f'Você digitou o dia: {dia}, portanto temos domingo!')
        case 2:
            print(f'Você digitou o dia: {dia}, portanto temos segunda-feira!')
        case 3:
            print(f'Você digitou o dia: {dia}, portanto temos terça-feira!')
        case 4:
            print(f'Você digitou o dia: {dia}, portanto temos quarta-feira!')
        case 5:
            print(f'Você digitou o dia: {dia}, portanto temos quinta-feira!')
        case 6:
            print(f'Você digitou o dia: {dia}, portanto temos sexta-feira!')
        case 7:
            print(f'Você digitou o dia: {dia}, portanto temos sábado!')
else:
    print('Digite um número válido!')

