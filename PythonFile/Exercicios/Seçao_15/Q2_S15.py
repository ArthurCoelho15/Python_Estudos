"""

Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
    a) Armazenar contato;
    b) Remover contato;
    c) Buscar contato; # Informa em que posição da agenda está o contato.
    d) Imprimir agenda; # Imprime os dados de todos os contatos da agenda.
    e) Imprimir contato. # Imprime os dados do contato informado pelo índice.

"""

from Q1_S15 import Pessoa

class Agenda:

    def __init__(self, nome, numero):
        self.__contatos: list[Pessoa] = []

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos





