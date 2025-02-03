"""

Q49. Faça um programa que leia o horário (hora, minuto e segundo) de início e duração, em segundos, de uma experiência biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.

"""

hora = int(input("A hora do experimento: "))
min = int(input("O minuto do experimento: "))
seg = int(input("O segundo do experimento: "))


print(f'Voce selecionou {hora}h {min}min {seg}seg -> {hora}:{min}:{seg}')

duracao = int(input("Digite a duracao em segundos: "))

print(f'Voce escolheu {duracao} segundos!')

if duracao == 60 and min != 59:
    min = min + 1
    print(f"\nO horário final do experimento foi {hora}h {min}min {seg}seg -> {hora}:{min}:{seg}")
elif duracao > 60:
    teste = duracao // 60
    if min + teste < 60:
        min = min + teste
        seg = seg + (duracao % 60)
        print(f"\nO horário final do experimento foi {hora}h {min}min {seg}seg -> {hora}:{min}:{seg}")
else:
    seg = seg + duracao
    print(f"\nO horário final do experimento foi {hora}h {min}min {seg}seg -> {hora}:{min}:{seg}")
