"""
RECEBENDO DADOS DO USUARIO

Formato antigo:

print('Qual é o seu nome? ')
nome = input()
print('Seja bem vindo %s' %nome)

* Cast = transformar um tipo de dado em outro
    por padrão o input transforma o dado recebido em string, por isso na linha
19 fiz o int() antes do input, pra transformar ele em int.
"""

# Entrada de dados

nome = input('Qual é o seu nome? ')

idade = int(input('Qual é a sua idade? '))

# Saida de dados

print(f'Seja bem-vindo(a) {nome}, voce tem {idade} e nasceu em {2025 - idade}')



