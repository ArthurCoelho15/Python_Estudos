"""

Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
    a) Armazenar contato (contato: Contato);
    b) Remover contato (contato: Contato);
    c) Buscar contato (nome: str); # Informa em que posição da agenda está o contato.
    d) Imprimir agenda; # Imprime os dados de todos os contatos da agenda.
    e) Imprimir contato (índice: int). # Imprime os dados do contato informado pelo índice.

"""
# Importando a biblioteca date, para trabalharmos com datas
from datetime import date
# Importando a classe Pessoa da questão anterior, para reutilizamos
from Q1_S15 import Pessoa

# Definindo a classe Agenda
class Agenda:

    # Definindo o construtor
    def __init__(self):
        # Definindo os contatos como sendo uma lista da classe Pessoa (reutilizando a questão anterior)
        self.__contatos: list[Pessoa] = []

    # Utilizando o decorador @property para globalizar a variável self.__contatos
    @property
    def contatos(self):
        return self.__contatos

    # Armazenando os contatos com a adição na lista
    def armazenar_contato(self, contato):
        self.contatos.append(contato)

    # Removendo os contatos com o remove da lista
    def remover_contato(self, contato):
        self.contatos.remove(contato)

    # Buscando contatos utilizando o enumerate (devolve índice e valor)
    def buscar_contato(self, nome):
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} esta na posicao {indice}')

    # Imprimindo a agenda utilizando a função imprimir da questão anterior (nome, email e data de nascimento)
    def imprimir_agenda(self):
        for contato in self.contatos:
            contato.imprimir()

    # Imprimindo apenas o contato escolhido utilizando a função imprimir da questão anterior (nome, email e data de nascimento)
    def imprimir_contato(self, indice: int):
        self.contatos[indice].imprimir()


def decisao(escolha):
    agenda: Agenda = Agenda()
    if escolha == '1':
        name = input('Digite seu nome: ')
        data = input('Digite sua data de nascimento (no formato dd/mm/aaaa): ')
        mail = input('Digite seu email: ')
        al = list(data.split('/'))
        contato = Pessoa(name, date(int(al[2]), int(al[1]), int(al[0])), mail)
        agenda.armazenar_contato(contato)
    elif escolha == '2':
        print(f'Funcionando {agenda.imprimir_agenda()}')



# Define que a partir daqui o código só funcionará se estivermos dando start no programa atual.
if __name__ == '__main__':
    agenda: Agenda = Agenda()
    while True:
        print('\n\n')
        num = input('Bem vindo a sua agenda!\n'
            'Escolha uma opção para continuar:\n'
            'Digite 1 para armazenar um contato\n'
            'Digite 2 para imprimir a agenda: ')
        if num != '2':
            pass
        else:
            agenda.armazenar_contato()