"""

FUNÇÕES:


    [1] Sintaxe:
        - nome_da_funcao -> SEMPRE em minúsculo, e se for nome composto separar por underline (Snake Case)
        - parametros_de_entrada -> Opcionais, se houver mais de 1 separar por vírgula.
        - bloco_da_funcao -> É onde o processo acontece
        - Parametros -> Variaveis declaradas na definição da função
        - Argumentos -> Dados passados durante a execução da função
            def nome_da_funcao(parametros_de_entrada):
                bloco da funcao
                return


    [2] Funções com parâmetros de entrada:
        def nome_da_funcao(parametro)
        - Ao definirmos uma função com parâmetros de entrada, tornamos OBRIGATÓRIO que esse parâmetro exista ao chamarmos essa função.
            (1) Podemos definir um valor padrão para o parâmetro, igualando ele ao valor
                - O valor padrão (default) tem que ser depois dos parâmetros não default
                    def nome_da_funcao(entrada1 = 1, entrada2) -> NOK
                    def nome_da_funcao(entrada2, entrada1 = 1) -> OK
        - Se informamos um número errado de parâmetro ou argumento, teremos TypeError.
            (2) Função com 2 entradas:
                def nome_da_funcao(entrada1, entrada2)
            (3) Função com 3 entradas:
                def nome_da_funcao(entrada1, entrada2, entrada3)


    [3] Utilizando funções dentro de outras:
        - Podemos utilizar uma função dentro de outra.
        - Atentar-se as variáveis globais e locais.
            - Priorizar a utilização de variáveis locais.
        (1) Introdução
        (2) Utilizando variável global na função
        (1) Utilizando variável local em outra função

"""

#1 SINTAXE:

"""
def cantar_parabens():
    print("Parabens para voce")
    print("nessa data querida")
    print("muitas felicidades")
    print("muitos anos de vida")

cantar_parabens()

def cantar_parabens():
    return 'Parabens para voce
nessa data querida
muitas felicidades
muitos anos de vida'

print(cantar_parabens())


from random import random

def aleatorio():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(aleatorio())
"""

#2 FUNÇÕES COM PARÂMETROS DE ENTRADA:

"""
# Função com 1 parâmetro:
def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(4))

# Função com parâmetro padrão (1):
def exponencial(numero, potencia = 2): # Caso o usuário não digite o valor da potência, usaremos 2 (ao quadrado) como padrão.
    return numero ** potencia

print(f'Sua potencia é: {exponencial(7)}')
print(f'Sua potencia é: {exponencial(2, 3)}')

# Função com 2 parâmetros (2):
def soma(a, b):
    return a + b

print(soma(10, 20))

# Função com 3 parâmetros (3):
def string(mult1, mult2, msg):
    return (mult1 + mult2) * msg

print(string(2, 5, 'Python '))
"""

#3 UTILIZANDO FUNÇÕES DENTRO DE OUTRAS:

"""
# Utilizando funções dentro de outras (1) - Introdução:
def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat(num1, num2, tipo = soma):
    return tipo(num1, num2)

print(mat(2, 3))
print(mat(5, 2, subtracao))
"""

# Utilizando funções dentro de outras (2) - Variáveis globais:
total1 = 0

def incrementa_global():
    global total1 # Indica que está utilizando uma variável global.
    total1 = total1 + 1
    return total1

print(incrementa_global())

# Utilizando funções dentro de outras (3) - Variáveis locais:

def fora():
    contador = 0

    def dentro():
        nonlocal contador # Não local, mas também não é global, é uma local de 'fora'.
        contador = contador + 1
        return contador
    return dentro()