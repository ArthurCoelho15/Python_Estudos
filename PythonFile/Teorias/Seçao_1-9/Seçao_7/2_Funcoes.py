"""

ARGS:
    - O *args é um parâmetro, como outro qualquer. Isso significa que você pode chamar ele de qualquer coisa, desde que comece com * asterístico.
    - O parâmetro *args é utilizado em uma função para fazer com que valores informados sejam registrados em uma tupla, e  não gere erro no código.
        - Vale lembrar que as Tuplas são imutáveis.


    [1] Utilizando o *args listas para ler listas nas funções:
        - Atenção a listas empacotadas.

KWARGS:
    - OS **kwargs é um parâmetro, como outro qualquer.
    - O parâmetro **kwargs é utilizado em uma função para fazer com que valores informados sejam registrados em um dicionário, e  não gere erro no código.
        - Os Kwargs exigem que utilizemos parâmetros nomeados, por causa da sua estrutura de dicionário.


    [1] Utilizando o **Kwargs listas para ler dicionário nas funções:
        (1) Com for
        (2) Com if
        (3) Desempacotamento


FUNÇÕES:
    [1] Ordem de declaração da sintaxe:
        (1) Parametros Obrigatórios;
        (2) *Args;
        (3) Parametros Não Obrigatórios (Default);
        (4) **Kwargs.
            def nome_da_funcao(parametro_obrigatorio, *args, parametro_default, **kwargs)

    [2] Desempacotamento:
        (1) Listas;
        (2) Tuplas;
        (3) Conjuntos / Sets;
        (4) Dicionários.
"""

# ARGS:

"""
def soma_todos_numeros(num1, num2=0, *args):
    return sum(args)

print(soma_todos_numeros(2))
print(soma_todos_numeros(2, 5))
print(soma_todos_numeros(7,5, 8))
"""
#1 ARGS COM LISTAS:
"""
def soma_lista(*args):
    return sum(args)

lista_numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_lista(lista_numeros)) # NOK -> Como o args bota o valor recebido em uma tupla, a função não consegue calcular um empacotamento.
print(soma_lista(*lista_numeros)) # OK -> o * antes da lista quer dizer que é para a função desempacotar antes de somar.
"""


# KWARGS:
"""
# Lendo dicionários (1):
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(arthur = 'verde', guilherme = 'roxo', lucas = 'preto', alan = 'azul')
"""
# Lendo dicionários (2):
"""
def cumprimento(**kwargs):
    if 'amigo' in kwargs and kwargs['amigo'] == 'Eai':
        return 'Eai amigao, tudo certo? Como vai a família?'
    elif 'amigo' in kwargs:
        return 'Olá, tudo certo?'
    return 'Bom dia'

print(cumprimento())
print(cumprimento(amigo = 'Eai'))
print(cumprimento(amigo = 'Oi'))
"""
# Lendo dicionários (3):

"""
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Arthur', 'sobrenome': 'Coelho'}

#print(mostra_nomes(nomes)) # Não funciona pois o dicionário ta empacotado
print(mostra_nomes(**nomes)) # Dicionário desempacotado
"""


# FUNÇÕES:

"""
def soma_multiplos(a, b, c):
    print(a + b + c)
"""
# Desempacotamento [1]:

"""
# Desempacotamento (1) - Listas:
lista = [1, 2, 3]
soma_multiplos(*lista) # 1 asterístico para desempacotar
"""
"""
# Desempacotamento (2) - Tuplas:
tupla = (1, 2, 3)
soma_multiplos(*tupla) # 1 asterístico para desempacotar
"""
"""
# Desempacotamento (3) - Sets:
set = {1, 2, 3}
soma_multiplos(*set) # 1 asterístico para desempacotar
"""
"""
# Desempacotamento (4) - Dicionários:
dicionario = dict(a = 1, b = 2, c = 3)
soma_multiplos(**dicionario) # 2 asterísticos para desempacotar
"""
