"""

GENERATORS / GENERATOR EXPRESSION:
    - Os Generators são as Tuple Comprehensions;
    - A partir do momento que utilizamos o dado ele apaga da memória;
    - O generator ocupa menos memória do que o List Comprehension, então é mais indicado utilizá-lo, é mais performático.

    1. Iterando no generator;
    2. Diferença na sintaxe do List Comprehension e Generator;
    3. Comparação de memória entre comprehensions e generator.


"""

#1 ITERANDO NO GENERATOR:

"""
gen = (x * 10 for x in range(1000))
#print(gen)
#print(type(gen))

for num in gen:
    print(num)
"""

#2 DIFERENÇA NA SINTAXE LIST COMP E GENERATOR:

"""
# List Comprehension:
list_comp = [x * 10 for x in range(1000)]
print(list_comp)
print(type(list_comp))
# Generator:
generator = (x * 10 for x in range(1000))
print(generator)
print(type(generator))
"""

#3 COMPARAÇÃO DE MEMÓRIA:
"""
from sys import getsizeof

# Gerando uma lista de números com List Comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehensions
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dict Comprehensions
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator Expression
generator = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List: {list_comp} bytes')
print(f'Set: {set_comp} bytes')
print(f'Dict: {dict_comp} bytes')
print(f'generator: {generator} bytes') # Muito mais performático
"""