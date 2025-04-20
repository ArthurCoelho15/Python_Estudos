"""

POO - ABSTRAÇÃO E ENCAPSULAMENTO
    - O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

    Abstração -> É o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário.
    Encapsulamento -> Manter as ações dentro da classe, o usuário não precisa saber como funciona.

"""


# O usuário não precisa saber todos os dados, tanto por questão de serem desnecessários ou por questões de privacidade.
# Todas as funções estão organizadas (encapsuladas) dentro da classe.
class Conta:

    contador = 1

    def __init__(self, titular, saldo, limite):
        self.__numero_conta = f'{Conta.contador:04d}' # Transformando a primeira conta em 0001, invés de 1.
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'O extrato do(a) {self.__titular} é de {self.__saldo} e tem {self.__limite} de limite')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor de depósito necessita ser positivo!')

    def sacar(self, valor):
        if self.__saldo > valor:
            if valor > 0:
                self.__saldo -= valor
            else:
                print('O valor de saque necessita ser positivo!')
        else:
            print('Saldo insuficiente.')

    def transferir(self, valor, conta_destino):
        # Retirando valor da conta atual (com validação)
        if self.__saldo > valor:
            if valor > 0:
                self.__saldo -= valor
                print(f'A transferência no valor de {valor} foi realizada para {conta_destino._Conta__titular}')
            else:
                print('O valor de transferência necessita ser positivo!')
        else:
            print('Saldo insuficiente.')

        # Adicionando o valor na conta destino
        conta_destino.__saldo += valor


# Criando contas e vendo as informações
conta1 = Conta('Arthur', 500, 2000)
print(conta1.__dict__)
conta2 = Conta('Nelson', 300, 3500)
print(conta2.__dict__)

# Vendo o extrato
conta1.extrato()

# Depositando e verificando o extrato
conta2.depositar(600)
conta2.extrato()

# Sacando e verificando o extrato
conta2.sacar(500)
conta2.extrato()

conta2.transferir(300, conta1)
conta1.extrato()
conta2.extrato()
