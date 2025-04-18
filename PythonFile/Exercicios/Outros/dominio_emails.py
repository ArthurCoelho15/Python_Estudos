from random import randint
from collections import Counter

gmail = '@gmail.com'
outlook = '@outlook.com'
hotmail = '@hotmail.com'

def get_domain(emails: str) -> str:
    """Pega cada linha do arquivo.txt, devide em uma lista de listas, essa lista de dentro estará dividido com o delimitador '@', o [-1] pega só o depois do '@'"""
    return emails.lower().split('@')[-1]
"""
pessoas = ['arthur', 'guilherme', 'lucas', 'alan', 'nelso', 'jenipapo', 'birunda', 'alandelao', 'anna', 'anapitu', 'kaline', 'maiscedo', 'stifmaster', 'rafa']
dominios = [gmail, outlook, hotmail]


with open('emails.txt', 'w') as arq:
    for i in range(len(pessoas)):
        dom = randint(0, 2)
        arq.write(f'{pessoas[i]}{dominios[dom]}\n')
        print(f'{pessoas[i]}{dominios[dom]}')
"""

with open('emails.txt', 'r') as lt_dom:
    domain_counts = Counter(get_domain(line.strip()) for line in lt_dom if '@' in line)
    print(dict(domain_counts))

