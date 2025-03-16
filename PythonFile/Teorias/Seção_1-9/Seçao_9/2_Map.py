"""

MAPS
    - Após utilizar a função map() depois da primeira utilização o resultado zera, apaga da memória.

    [1] Sintaxe:
        map(função, iterável)

"""

import math
areas = []


# Forma 1:

def area(r):
    return round(math.pi * (r ** 2), 2)

raios = [2, 5, 10, 44]

for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 - Utilizando map:

areas_map = map(area, raios)

print(areas_map)
print(list(areas_map))

# Forma 3 - Map com lambda:
print(list(map(lambda r: round(math.pi * (r ** 2), 2), raios)))