"""

Faça um programa que receba do usuario o nome de um arquivo texto e mostre na tela quantas linhas este arquivo possui.


"""

nome_arq = input('Digite o nome do arquivo que voce deseja saber a quantidade de linhas: ')

# Fiz dessa forma
"""
with open(nome_arq, 'r') as arq_user:
    print(len(arq_user.readlines()))
"""

# Chat GPT falou que era melhor dessa forma por questão de memória:
with open(nome_arq, 'r') as arquivo:
    quantidade_linhas = sum(1 for linha in arquivo)

print(f"O arquivo tem {quantidade_linhas} linhas.")
