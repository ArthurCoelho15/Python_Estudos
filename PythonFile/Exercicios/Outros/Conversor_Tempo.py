"""

Crie um programa que receba um valor de segundos e converta para o correspondente no formato hora:minuto:segundo

"""

segundos = int(input("Digite um valor em segundos: "))

horas = segundos // 3600
segundos = segundos - horas * 3600
minutos = int(segundos // 60)
segundos = segundos - minutos * 60

print("{}:{}:{}".format(horas, minutos, segundos))
