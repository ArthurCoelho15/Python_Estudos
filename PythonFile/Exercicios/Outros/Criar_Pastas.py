import os

delta = range(1, 7)

# Criando arquivo txt
with open(f'backup.txt', 'x+') as bkp:
    for mq in delta:
        bkp.write(f'MD teste_0{mq}\n')


# Transformando o arquivo txt em bat para execução
os.rename('backup.txt', 'backup.bat')


# Executando o bat para a criação das pastas testes
caminho_bat = r'"C:\Users\arthu\OneDrive\Área de Trabalho\Faculdade\Programação\PythonUdemy\PythonFile\Exercicios\Outros\backup.bat"'
os.system(caminho_bat)

# Apagando a pasta bat, para não poluir o diretório.
os.remove('backup.bat')

# Criando pastas 1 e 2 de cada pasta teste
for i in delta:
    with open(rf'teste_0{i}\cria_qtd.txt', 'x+') as mq_ls:
        for qtd in range (1,3):
            mq_ls.write(f'cd teste_0{i}\n')
            mq_ls.write(f'MD {qtd}\n')
    # Transformando o arquivo txt em bat para execução
    os.rename(rf'teste_0{i}\cria_qtd.txt', rf'teste_0{i}\cria_qtd.bat')
    # Executando o arquivo para para criar as pastas 1 e 2
    os.system(rf'teste_0{i}\cria_qtd.bat')
    # Apagando a pasta bat, para não poluir o diretório.
    os.remove(rf'teste_0{i}\cria_qtd.bat')
