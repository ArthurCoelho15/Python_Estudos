"""

LOOP WHILE:
    Forma geral:
        while expressão booleana:
            //execução do looping
        OBS: O bloco do while será repetida enquanto a expressão booleana for verdadeira.
            Expressão booleana é toda expressão que o resultado é verdadeiro ou falso.

* SAINDO DE Loops *
    Pode-se utilizar a função 'break' para sair de loops de forma planejada.
"""

num = 0

# While
while num <= 10:
    print(num)
    num = num + 1

# Breaks
while True:
    num = num + 1
    if num == 10:
        break
    else:
        print(num)
print("Saindo do looping! ")