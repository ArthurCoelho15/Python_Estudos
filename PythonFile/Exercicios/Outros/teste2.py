lista = []
resultado = []
i = 0

size = int(input())
i = 0

dict = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII",
        8: "VIII", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
        400: "CD", 500: "D", 900: "CM", 1000: "M" }

def roman(lista):
    for romanos in range(0, len(lista)):
        if lista[romanos] not in dict:
            while lista[romanos] > 1:
                global i
                lista[romanos] = lista[romanos] / 10
                i = i + 1
                for divisao in range(0, i+1):
                    dividido = lista[romanos][0] * 10 * i
                    lista[romanos] = dividido
        else:
            lista[romanos] = dict.get(lista[romanos])

        print(lista[romanos])
for i in range(0,size):
    n = int(input())
    lista.append(n)

roman(lista)