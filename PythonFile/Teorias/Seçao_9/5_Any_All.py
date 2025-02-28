"""

ALL:
    - Retorna True se todos os elementos do iterável são verdadeiros, ou se o iterável está vazio.
        [0, 1, 2, 3] -> False, 0 é False
        [1, 2, 3] -> True, todos os elementos são considerados True
        [] -> True, iterável sem elementos

ANY:
    - Retorna True se pelo menos um dos elementos do iterável são verdadeiros;
    - Se o iterável estiver vazio retorna False.


    OBS: A diferença principal entre o any e all é que quando o iterável está vazio:
        - All: True
        - Any: False
"""

# ALL:
all_True = ['Carlos', 'Camila', 'Carla', 'Clovis']
all_False = ['Carlos', 'Camila', 'Denis', 'Clovis']

print(all([nome[0] == 'C' for nome in all_True])) # Verifica a primeira letra de cada string
print(all([nome[0] == 'C' for nome in all_False])) # Verifica a primeira letra de cada string

print(all(num for num in [0, 2, 4, 6, 8, 9] if num % 2 == 0)) # 9 é impar, False

# ANY:
any_True = ['Carlos', 'Camila', 'Carla', 'Clovis']
any_True1 = ['Carlos', 'Camila', 'Denis', 'Clovis']

print(any([nome[0] == 'C' for nome in any_True]))
print(any([nome[0] == 'C' for nome in any_True1]))

print(any(num for num in [0, 2, 4, 6, 8, 9] if num % 2 == 0)) # 9 é impar, mesmo assim é True