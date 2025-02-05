"""

Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).

"""

inicio = int(input('Digite 0 para iniciar! '))

while inicio < 100_000:
    inicio = inicio + 1000
    print(inicio)