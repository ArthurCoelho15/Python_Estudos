"""

ESTRUTURAS CONDICIONAIS

If:
    [1] If significa 'se', atribuimos uma condição a determinada variável.
    [2] o If se restringe a primeira condição, pra seguir a PEP8.

Elif:
    [1] Elif é o if sendo que para as outras condições

Else:
    [1] Else significa 'se', parecido com o if,
porém é utilizado no fim da condição, tem que ser a última condição.
"""
idade = int(input("Digite sua idade "))

# IF [1]
if idade < 18:
    print("Idade menor que 18!")
elif idade == 18:
    print("Idade igual a 18!")
else:
    print("Idade maior que 18!")