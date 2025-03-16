"""

ESTRUTURAS LÓGICAS:
    [1] and (e)  -> Operadores binário
    [2] or (ou) -> Operadores binário
    [3] not (nao) -> Operadores unitários
    [4] is (é) -> Operadores binários

    1. Ambos os valores precisam ser True
    2. Um ou outro valor precisa ser True
    3. O valor do booleano é invertido, True vira False e False vira True.
    4.

"""

ativo = True
logado = False

if ativo and logado:
    print('Bem vindo usuário!')
elif logado is False:
    print('Entre na sua conta.')
else:
    print('Voce precisa ativar a sua conta. Por favor, cheque seu email.')
    