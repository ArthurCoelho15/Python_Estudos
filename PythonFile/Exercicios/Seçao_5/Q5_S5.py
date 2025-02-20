"""

Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta "Qual é a soma de a + b?".
Peça a resposta, faça 5 perguntas e mostre as respostas corretas e incorretas, no final mostre a quantidade de acertos.

"""

import random

i = 0
contador = 0

while i < 5:
    a = random.randrange(1,100)
    b = random.randrange(1, 100)
    P1 = int(input(f"Qual é o valor de {a} + {b}? "))
    if P1 == (a + b):
        print("Você acertou!")
        contador = contador + 1
    else:
        print(f"Errou! Você escreveu {P1}, mas a resposta é {a + b}")
    i = i + 1

print(f'Você acertou {contador} perguntas')
