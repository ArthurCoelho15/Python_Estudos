"""

Faça um programa que tenha uma função que recebe uma data no formato string e imprima ela por extenso
    - Ex: recebe '01/01/2024' e imprime '1 de janeiro de 2024'.

"""

meses = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}

def mes_extenso(data):
    global meses

    data_corrigida = data.split('/')

    dia = int(data_corrigida[0])
    mes = meses[data_corrigida[1]]
    ano = data_corrigida[2]
    return f'A data por extenso é: {dia} de {mes} de {ano}'

usuario = str(input("Digite uma data no formato XX/YY/ZZZZ: "))

print(mes_extenso(usuario))
