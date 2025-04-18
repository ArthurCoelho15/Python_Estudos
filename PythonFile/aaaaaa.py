lista = []
certo = []

for num in range(1, 101):
    az = 1
    ve = 2
    verde = 3
    lista.extend([az,ve,verde])
    if sum(lista) >= 100:
        break
print(lista)
print(sum(lista))
print(len(lista))

