# Abaixo segue um exemplo de código que você pode ou não utilizar
segundos = int(input())

# TODO: Complete os espaços em branco com as operações que calculam a duração em segundos.
horas = segundos // 3600
segundos = segundos - horas * 3600
minutos = int(segundos // 60)
segundos = segundos - minutos * 60

# DICA: O Método format() cria uma String que contém campos entre chaves que são
# substituídas pelos argumentos do format.
print("{}:{}:{}".format(horas, minutos, segundos))
