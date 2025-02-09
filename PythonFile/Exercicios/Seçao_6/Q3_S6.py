"""

Peça ao usuário um número inteiro entre 100 e 100_000, em seguida imprima os algarismos que compõem esse número de forma individual

"""

num = int(input("Digite um numero entre 100 e 100000: "))
lista = []
algarismos = 0

while (num < 100) or (num > 100_000):
    num = int(input("Digite um número válido: "))

for i in range(0,len(str(num))):
    string = str(num)
    lista.append(string[i])
    while algarismos < len(lista):
        print(f'O {algarismos + 1}º algarimso é {lista[algarismos]}')
        algarismos = algarismos + 1
