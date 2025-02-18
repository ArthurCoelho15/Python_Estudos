lista = []
resultado = []
i = 0

size = int(input("Digite a quantidade de números: "))

dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
        90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

def int_to_roman(num):
    roman_str = ""
    for value in sorted(dict.keys(), reverse=True):  # Itera pelos valores do dicionário em ordem decrescente
        while num >= value:
            roman_str += dict[value]
            num -= value
    return roman_str

def roman(lista):
    for num in lista:
        print(int_to_roman(num))  # Converte e imprime o número em romano

for i in range(size):
    n = int(input(f"Digite o número {i + 1}: "))
    lista.append(n)

roman(lista)