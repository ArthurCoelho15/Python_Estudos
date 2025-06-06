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

# Define que a partir daqui o código só funcionará se estivermos dando start no programa atual.
if __name__ == '__main__':
    # define os contatos, utilizando a classe Pessoa
    contato1 = Pessoa('Arthur Coelho', date(2003, 4, 15), 'arthur@gmail.com')
    contato2 = Pessoa('Guilherme Henrique', date(2004, 1, 15), 'guilherme@gmail.com')
    contato3 = Pessoa('Lucas Muniz', date(2003, 4, 24), 'lucas@gmail.com')

    # Instancia a classe agenda, para poder ser utilizada nas demais funções.
    agenda: Agenda = Agenda()

    # Armazenando os contatos anteriormente definidos, utilizando a função armazenar_contato
    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)

    # Imprimindo a agenda completa, utilizando a função imprimir_agenda
    agenda.imprimir_agenda()

    # Buscando contato pelo nome, utilizando a função buscar_contato, a função irá devolver o nome e índice
    agenda.buscar_contato('Arthur Coelho')

    # Imprimindo as informações do contato utilizando o índice como ferramenta de busca, continuando a linha anterior do buscar_contato
    agenda.imprimir_contato(2)

    # Removendo o contato definido na variável
    agenda.remover_contato(contato3)

    # Imprimindo a agenda completa após a sequência de modificações
    agenda.imprimir_agenda()
