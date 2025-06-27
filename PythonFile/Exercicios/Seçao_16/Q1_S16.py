"""

 1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.

"""

class Veiculo:

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.__marca: str = marca
        self.__modelo: str = modelo
        self.__ano: int = ano

    def __str__(self):
        return f'O seu veiculo eh da {self.__marca} e eh um {self.__modelo} do ano {self.__ano}'

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self: object, marca: str) -> None:
        self.__marca = marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self: object, modelo: str) -> None:
        self.__modelo = modelo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self: object, ano: int) -> None:
        self.__ano = ano

    def imprimir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')

if __name__ == '__main__':

    carro1: Veiculo = Veiculo('Jeep', 'Compass', '2020')
    print(carro1)

    print(carro1.__dict__)
    carro1.ano = 2012
    print(carro1.__dict__)

    print('')
    carro1.imprimir()
