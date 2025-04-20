"""

Crie a classe televisão com os atributos Status, volume, canal e controle remoto. De forma que:
    a) Devemos poder ligar, desligar e gerenciar som e canais pela televisão e controle remoto;
    b) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez,
    mas também permitir que seja informado um número de canal para efetuar a troca.

"""
from datetime import date

from Q1_S15 import Pessoa


class Agenda:

    def __init__(self):
        self.__contatos = []

    @property
    def contatos(self):
        return self.__contatos

    def armazenar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, contato):
        self.contatos.remove(contato)

    def buscar_contato(self, nome):
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} esta na posicao {indice}')

    def imprimir_agenda(self):
        for contato in self.contatos:
            contato.imprimir()

    def imprimir_contato(self, indice: int):
        self.contatos[indice].imprimir()



contato1 = Pessoa('Felicity Jones', date(1987, 7, 22), 'felicity@gmail.com')
contato2 = Pessoa('Angelina Jolie', date(1984, 3, 6), 'angelina@gmail.com')
contato3 = Pessoa('Ray Sychev', date(1981, 8, 18), 'ray@gmail.com')

agenda: Agenda = Agenda()

agenda.armazenar_contato(contato1)
agenda.armazenar_contato(contato2)
agenda.armazenar_contato(contato3)

agenda.imprimir_agenda()

agenda.buscar_contato('Ray Sychev')

agenda.imprimir_contato(2)

agenda.remover_contato(contato3)

agenda.imprimir_agenda()


contato1 = Pessoa('Felicity Jones', date(1987, 7, 22), 'felicity@gmail.com')
#contato2 = Pessoa('Angelina Jolie', date(1984, 3, 6), 'angelina@gmail.com')
#contato3 = Pessoa('Ray Sychev', date(1981, 8, 18), 'ray@gmail.com')

agenda: Agenda = Agenda()

agenda.armazenar_contato(contato1)
#agenda.armazenar_contato(contato2)
#agenda.armazenar_contato(contato3)

agenda.imprimir_agenda()

agenda.buscar_contato('Ray Sychev')

agenda.imprimir_contato(2)

agenda.remover_contato(contato3)

agenda.imprimir_agenda()


