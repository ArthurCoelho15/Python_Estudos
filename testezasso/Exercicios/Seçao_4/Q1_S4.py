"""

Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

"""

numero1 = input("Digite o primeiro numero: ")
numero2 = input("Digite o segundo numero: ")

if numero1 > numero2:
    print(f'O numero {numero1} é maior que o {numero2}')
elif numero1 < numero2:
    print(f'O numero {numero2} é maior que o {numero1}')
else:
    print('Ambos os numeros sao iguais!')