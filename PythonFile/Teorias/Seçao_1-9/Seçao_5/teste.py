n = int(input())
lista = []

binario = bin(n)

for bin in binario:
    lista.append(bin)

print(lista)
while lista[0] != '1':
    lista.pop(0)

print(lista.count('1'))
for i in lista:
    print(lista.index('1') + 1)
    lista[lista.index('1')] = 0

    if '1' not in lista:
        break




