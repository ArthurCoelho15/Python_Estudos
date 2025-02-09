"""

Leia um número inteiro positivo de um usuário, então calcule a sequência de Fibonacci até o primeiro número superior ao número lido.
    - Exemplo: Se o usuário informou o número 30:
        Sequência impressa: 0 1 1 2 3 5 8 13 21 34

"""

i = 1
fibonacci = [0, 1]

num = int(input("Digite um número positivo maior que 0: "))

while True:
    #print(fibonacci)
    fibonacci.append(fibonacci[i] + fibonacci[i-1])
    print(fibonacci[i])
    if fibonacci[i+1] - num > 0:
        print(fibonacci)
        break
    i = i + 1
