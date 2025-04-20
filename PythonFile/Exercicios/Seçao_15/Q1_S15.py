"""

Crie uma classe pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e setters para
os atributos, e um método para imprimir os dados de uma pessoa.

"""

from datetime import date

class Pessoa:

    def __init__(self, nome: str, nascimento: date, email: str ) -> None:
        self.__nome = nome
        self.__nascimento = nascimento
        self.__email = email

    @property
    def nome(self) -> str:
        return self.__nome.title()

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nascimento(self) -> date:
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento: date) -> None:
        self.__nascimento = nascimento

    @property
    def email(self) -> str:
        return self.__email.lower()

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    def imprimir(self):
        print(f'Nome: {self.nome}')
        print(f'data de nascimento: {self.nascimento.strftime('%d/%m/%Y')}')
        print(f'Email: {self.email}')

name = input('Digite seu nome: ')
data = input('Digite sua data de nascimento: ')
mail = input('Digite seu email: ')

al = list(data.split('/'))

p1 = Pessoa(name, date(int(al[2]), int(al[1]), int(al[0])), mail)

p1.imprimir()
