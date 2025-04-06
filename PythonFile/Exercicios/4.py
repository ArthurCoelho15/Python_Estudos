notas = [73, 67, 38, 33]
lista_cincao = []

print(f'Notas originais: {notas}')

def mult_5(x):
    lista_cincao.clear()
    i = 1
    cincao  = 5
    while x > cincao:
        cincao = 5 * i
        i += 1
        lista_cincao.append(cincao)
    if max(lista_cincao) - x < 3:
        x = max(lista_cincao)
    return x

for i in range(len(notas)):
    if notas[i] < 38:
        continue
    else:
        notas[i] = mult_5(notas[i])

print(f'Notas arredondadas: {notas}')
