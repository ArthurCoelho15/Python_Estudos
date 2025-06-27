"""

 2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.

"""

from Q1_S16 import Veiculo


class Carro(Veiculo):

    def __init__(self, marca: str, modelo: str, ano: int, qtd_portas: int) -> None:
        super().__init__(marca, modelo, ano)
        self.__qtd_portas: int = qtd_portas

    def __str__(self) -> str:
        return f'O {self.modelo} da marca {self.marca} tem {self.qtd_portas} portas!'

    @property
    def qtd_portas(self):
        return self.__qtd_portas

    @qtd_portas.setter
    def qtd_portas(self, qtd_portas):
        self.__qtd_portas = qtd_portas

    def imprimir(self):
        super().imprimir()
        return f'Portas: {self.__qtd_portas}'


if __name__ == '__main__':
    c: Carro = Carro('Stellantis', 'Renegade', 2025, 5)

    print(c)

    print(c.__dict__)
    c.qtd_portas = 2
    print(c)
    print(c.__dict__)
    print('')
    print(c.imprimir())
