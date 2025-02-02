"""
TIPO NUMERICO1:
    São, a grosso modo valores inteiros

    [1] % -> retorna o resto da divisao
        5 % 2 = 1
    [2] // -> retorna o inteiro da divisao
        5 // 2 = 2
    [3] ** -> potencia
        8 ** 2 = 64
    [4] _ -> pode ser usado para facilitar identificaçao
        10000 = 10_000
    [5] += -> utilizado para incrementar igual o num = num + 1
    [6] type -> funcao que indica qual o tipo de variavel (int, float, double, etc...)

OBS:

    [1] Na programaçao a virgula nao separa casas decimais, e o ponto,a virgula
separa variaveis
    [2] Na programaçao usamos o '=' para atribuir valor a variavel e
'==' para comparar.


TIPO FLOAT:
    São valores decimais

    [1] Ao convertemos valores float para inteiro perdemos precisao (perdemos o decimal dele)

TIPO BOOLEANO:
    São valores verdadeiro ou falso
    Necessita escrever com a letra maiuscula (True ou False)

    [1] negação (not) -> nega o valor, se temos True ele transforma em False
    [2] Ou (or) -> depende de dois valores, um ou outro deve ser verdadeiro
    [3] E (and) -> depende de dois valores, ambos devem ser verdadeiros

TIPO STRING:
    [1] As strings sao basicamente um mapeamento da palavra
            Ex: Arthur Nelson
                ['A','r','t','h,'u','r',' ','N','e','l','s','o','n']
                ['0','1','2','3,'4','5','6','7','8','9','10','11','12']
        Podemos inverter a string [::-1] -> [inicio:fim:ordem] (nao preenchemos)
    [2] Sempre que estiver entre aspas simples, duplas ou triplas
        'string' , "string" , ''string'', ""string"", '''string'''
    [3] upper() -> para deixar a string toda em maiusculo
    [4] lower() -> pra deixar a string toda em minusculo
    [5] title() -> pra deixar so a primeira em maiusculo
    [6] split() -> transforma em uma lista de strings
    [7] replace() -> troca um valor da string por outro
        Atentar-se que há a dif entre maiusculo e minusculo
"""

# Tipo numerico [5]
num = 5
num += 1
print(num)


# OBS [1]
num1, num2 = 1, 5
print(num1, num2)


# Tipo booleano [1]
logado = False
print(not logado)
# Tipo booleano [2]
logado2 = True
print(logado or logado2)
# Tipo booleano [3]
print(logado and logado2)


# Tipo string [1]
nome = 'Arthur Nelson'
print(nome[7:13])
print(nome[::-1])
# Tipo string [3]
print(nome.upper())
# Tipo string [4]
print(nome.lower())
# Tipo string [5]
nome2 = 'aRTHUR nELSON2'
print(nome2.title())
# Tipo string [6]
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])
# Tipo string [7]
print(nome.replace('N','J'))