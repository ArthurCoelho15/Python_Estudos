"""

Faça um programa que:
    a) Crie e abra um arquivo de texto;
    b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário digite '0' para parar a gravação;
    c) Feche o arquivo;
    d) Abra e leia o arquivo e escreva na tela todos os caracteres armazenados.

"""

with open('Q1_S12.txt', 'w+') as arq_q1_S12:
    while True:
        caractere = input('Informe um caractere: ')
        if caractere != '0':
            arq_q1_S12.write(f'{caractere}\n')
        else:
            break

with open('Q1_S12.txt', 'r') as arq_ler:
    print(f'O arquivo: {arq_ler} tem o seguinte texto:\n\n{arq_ler.read()}')
