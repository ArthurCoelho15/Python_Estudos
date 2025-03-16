"""

RAISE:
    - Lança exceções
    - Não é uma função, é uma palavra reservada.
    - Podemos utilizar para criar nossas próprias exceções e tipos de erros
    - Assim como o return, o raise finaliza a função, depois dele nada é executado.

    1. Sintaxe:
        - raise TipoDoErro('Mensagem de erro')

    2. Problemas:

"""


def colorir(texto, cor):
    cores = ('verde', 'azul', 'amarelo')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser string!')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser string!')
    if cor not in cores:
        raise ValueError(f'Escolha a cor valida entre {cores}')
    print(f'O texto {texto} sera impresso com a cor {cor}')

# Exemplo correto:
colorir('Nelson', 'azul')

# Problema 1:
#colorir(4, 'azul')

# Problema 2:
#colorir('Nelson', 5)

# Problema 3:
#colorir('Nelson', 'preto')
