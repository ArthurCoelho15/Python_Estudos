"""

Escreva um programa que leia um número inteiro positivo N e em seguida imprima N linhas do chamado Triângulo de Floyd.
    - Ex: Para N = 6 teremos:
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
        16 17 18 19 20 21

"""

num = int(input("Digite o número de linhas: "))
a = 1

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(f'{a} ', end="")
        a = a + 1
    print()
