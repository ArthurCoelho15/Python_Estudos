"""

FUNÇÕES LAMBDA
    - São funções sem nome, ou seja, funções anônimas;
    - Usa-se bastante a função lambda como key;

    [1] Sintaxe:
        lambda nome_do_parametro_a_receber: //função
"""


def funcao(x):
    return 3 * x + 1

print(funcao(9))

funcao_lambda = lambda x: 3 * x + 1
print(funcao_lambda(9))

def geradora_funcao_quadradica(a, b, c):
    return lambda y: a * y ** 2 + b * y + c

teste = geradora_funcao_quadradica(2, 3, -5)
"""
aqui estamos definindo os parametros a, b e c
"""

print(teste(2))
"""
aqui estamos definindo o parametro y
"""

print(geradora_funcao_quadradica(2, 3, -5)(2))
"""
aqui estamos printando e já definindo o parametro a, b, c e y
"""
