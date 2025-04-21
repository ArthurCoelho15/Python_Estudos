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

# Define que a partir daqui o código só funcionará se estivermos dando start no programa atual.
if __name__ == '__main__':
    # define os contatos, utilizando a
    contato1 = Pessoa('Arthur Coelho', date(2003, 4, 15), 'arthur@gmail.com')
    contato2 = Pessoa('Guilherme Henrique', date(2004, 1, 15), 'guilherme@gmail.com')
    contato3 = Pessoa('Lucas Muniz', date(2003, 4, 24), 'lucas@gmail.com')

    # Instancia a classe agenda, para poder ser utilizada nas demais funções.
    agenda: Agenda = Agenda()

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)

    agenda.imprimir_agenda()

    agenda.buscar_contato('Arthur Coelho')

    agenda.imprimir_contato(2)

    agenda.remover_contato(contato3)

    agenda.imprimir_agenda()




