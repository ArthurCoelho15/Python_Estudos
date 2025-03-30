"""

MÓDULOS PERSONALIZADOS:
    - Podemos executar funções de outros módulos utilizando o import

"""

import os

maquina = []
vez = [1, 2]

for i in range(1, 7):
    with open(f'laser {i}.txt', 'x+') as ls:
        while True:
            fruta = input('Digite uma fruta ou sair: ')
            if fruta != 'sair':
                dub.write('MD ' + fruta + '\n')
            else:
                break

    with open('Asdrubal.txt', 'r') as dub1:
        leia = dub1.read()
        print(leia)

    os.rename('Asdrubal.txt', 'Asdrubal.bat')


caminho_bat = r'"C:\Users\arthu\OneDrive\Área de Trabalho\Faculdade\Programação\PythonUdemy\PythonFile\Exercicios\Outros\backup.bat"'