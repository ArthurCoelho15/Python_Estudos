"""

MANIPULANDO DATA E HORA:
    - Biblioteca 'datetime':
        [1] Funções:
            (1) datetime.now() -> Pega a data e horários atuais (mesma coisa do today) -> Conseguimos especificar fuso horário
            (2) datetime.today() -> Pega apenas a data de hoje (mesma coisa do today) -> Não conseguimos especificar fuso horário
            (3) datime.timedelta(argumento) -> definimos um tempo para variar
            (4) datetime.combine(
            (5) weekday -> retorna o dia da semana (segunda = 0, terça = 1, quarta = 2, etc...)
            (6) datetime.time(hora, minuto, segundo)
        [2] Formatação:
            (1) strftime('%d/%m/%Y') -> devolve a data no formato dd/mm/aaaa
            (2) strftime('%d/%m/%y') -> devolve a data no formato dd/mm/aa
            (3) strftime('%d/%B/%Y') -> devolve a data no formato dd/nome_mes/aaaa
            (4) strftime('%d/%b/%Y') -> devolve a data no formato dd/iniciai_mes/aaaa
            (5) strftime('%B') -> devolve apenas o mês

    - Biblioteca 'timeit':
        [1] Sintaxe:
            (1) timeit.timeit(função, number=qtd_ocorrencias)
            (2) timeit.timeit(functools.partial(funcao, parametro), number=qtd_ocorrencias)

"""

from textblob import TextBlob
import datetime
import functools
import timeit

from datetime import date
from time import strftime

agora = datetime.datetime.now()

""" teste = date.today()"""

# Definindo a data do meu aniversario:
aniversario = datetime.datetime(2026, 4, 15, 0,)

# Definindo a variável para calcular o delta de hoje até meu aniversário do próximo ano
delta_aniversario = aniversario - agora

# Definindo um delta de tempo para acrescentar na data de hoje
delta_tempo = datetime.timedelta(minutes=5)


print(agora)
print(f'A data de agora formatada1 é: {agora.strftime('%d/%m/%Y')}')
print(f'A data de agora formatada2 é: {agora.strftime('%d/%m/%y')}')
print(aniversario)
print(f'A data de aniversario formatada3 é: {aniversario.strftime('%d/%B/%Y')}')
print(f'A data de aniversario formatada4 é: {aniversario.strftime('%d/%b/%Y')}')
print(f'A data de aniversario [APENAS MÊS] formatada5 é: {aniversario.strftime('%B')}')


print(delta_aniversario)

# Verificando o tempo até meu aniversário do próximo ano
print(f'Faltam {delta_aniversario.days} dias e {delta_aniversario.seconds // 3600} horas para meu aniversário')

# Testando variação de data/hora
print(f'São {agora} e daqui a 5 minutos vai ser {agora + delta_tempo}')

# TRABALHANDO APENAS COM A HORA:

