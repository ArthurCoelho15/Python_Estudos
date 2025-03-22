"""

TRY / EXCEPT:
    Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
    Prevenindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

    1. FORMA GERAL:

try:
    // execução problemática
except:
    // oque deve ser feito em caso de problemas

        [1] Tratando erros genéricos;
        [2] Tratando erros específicos. -> Mais recomendado
            - Normal:
                - Recomendada para o usuário.
            - Promovendo log:
                - Recomendada para o dev, registro.

    2. UTILIZANDO O BLOCO EM FUNÇÕES
        [1] Tratando dados de entrada.



ELSE / FINALLY:
    Else -> Tratamento para caso não ocorra o erro
    Finally -> Sempre será executado, independentemente de erro.
        - Geralmente utilizado para fechar ou desalocar recursos
        (interromper a conexão com banco de dados, fechar um arquivo que foi aberto para leitura/escrita).

    A função do usuário é destruir o sistema:
        - Pedimos uma entrada de int e o usuario digita uma string
            - Devemos tratar esse erro

"""

# TRY / EXCEPT:

#1 FORMA GERAL:
"""
# Tratando erros genericos [1]:
try:
    arthur() # NameError (arthur()) nao está definido
except:
    print("funcao nao definida, name error")
"""
"""
# Tratando erros especificos [2] - Normal:
try:
    len(5)
except TypeError:
    print('A aplicação gerou TypeError')
"""
"""
# Tratando erros especificos [2] - Log:
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou TypeError: {err}')
"""

#2 UTILIZANDO O BLOCO EM FUNÇÕES:

"""
def testa_dict(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as err1:
        return f"KeyError: {err1}"
    except TypeError as err2:
        return f"TypeError: {err2}"
    except:
        return None

dic = {"nome": "Arthur"}

print(testa_dict(dic,"nome"))
"""

# Tratando dados de entrada [1] - Exemplo 1:

"""
def dividir(a, b):
    try:
        return int(a) / int(b) # importante fazer o cast pois o input é str
    except ValueError:
        return 'Numero inválido'
    except ZeroDivisionError:
        return 'Nao é possível dividir por zero'

num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundoo numero: ')

print(dividir(num1, num2))
"""

# Tratando dados de entrada [1] - Exemplo 2:
"""
def dividir(a, b):
    try:
        return int(a) / int(b) # importante fazer o cast pois o input é str
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundoo numero: ')

print(dividir(num1, num2))
"""



# ELSE / FINALLY:

"""
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Voce nao digitou um valor valido!')
else:
    print(f'Voce digitou {num}')
finally:
    print('Executando o finally')
"""