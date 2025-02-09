"""

Faça um programa que calcule a soma de todos os números impares e depois pares de 0 até o valor que o usuário digitar.

"""


def soma_impares(numeros):
    impar = 0
    for num in numeros:
        if num % 2 != 0:
            impar = impar + num
    return impar

def soma_pares(numeros):
    par = 0
    for num in numeros:
        if num % 2 == 0:
            par = par + num
    return par

num_final = int(input("Digite um número: "))

lista = list(range(1,num_final+1))
print(lista)

print(f'A soma de todos os numeros impares até o {num_final} é: {soma_impares(lista)}')
print(f'A soma de todos os numeros pares até o {num_final} é: {soma_pares(lista)}')

