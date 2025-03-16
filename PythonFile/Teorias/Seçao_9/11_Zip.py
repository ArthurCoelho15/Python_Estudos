"""

ZIP:
    - Após utilizar a função zip() depois da primeira utilização o resultado zera, apaga da memória.
    - O zip utiliza como parâmetro o menor tamanho do iterável, por exemplo:
        temos 3 listas:
            lista 1 => [1, 2, 3]
            lista 2 => ['a', 'b', 'c', 'd', 'e']
            lista 3 => ['w', 'x', 'y', 'z']

            print(list(zip(lista1, lista2, lista3)))
            output ->   [(1, 'a', 'w'), (2, 'b', 'x'), (3, 'c', 'y')]
                - Ignorou o 4º e 5º parametro da lista2 e o 4º parametro da lista3, pois se adequou ao tamanho da lista1
                    - independentemente da ordem que escrever no zip -> zip(lista3, lista2, lista1) ou zip(lista2, lista1, lista3) mesma coisa.


    1. Sintaxe:
        map(iteravel_1, iterável_2, ..., iteravel_n-1)

    2. Desempacotamento de zip:
        - Funciona de forma semelhante ao *args

    3. Iterando com zip:
        [1] Utilizando funções lambda;
        [2] Utilizando funções lambda
            - Com função map
"""

#1 SINTAXE:

"""
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]

zip1 = zip(lista1, lista2)
zip2 = zip(lista1, lista2, 'XYZ')

print(list(zip1))
print(list(zip2))
print(type(zip1))
"""

#2 DESEMPACOTAMENTO DE ZIP:
"""
dados = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

num, letras = zip(*dados)

print(list(num))
print(list(letras))
"""

#3 ITERANDO COM ZIP:

# Utilizando função lambda [1]:

prova1 = [80, 91, 78]
prova2 = [92, 86, 69]
alunos = ['Lucas', 'Guilherme', 'Alan']

maior_nota = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print('Maiores notas:', maior_nota)

menor_nota = {dado[0]: min(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print('Menores notas:', menor_nota)

media_notas = {dado[0]: (dado[1] + dado[2])/2 for dado in zip(alunos, prova1, prova2)}
print('Media final:', media_notas)

# Utilizando funcao lambda [2]:

maior = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print('aqui', dict(maior))