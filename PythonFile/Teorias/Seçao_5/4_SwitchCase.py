"""

SWITCH CASE:
    No python não temos a função Switch() e case() como nas outras linguagens, mas a partir da versão 3.10 surgiu uma funcionalidade idêntica.
        Ex: Match e Case()
    Podemos utilizar para condições programadas, onde não há a utilização de outro input além do mapeado.

"""

opcao = int(input("Digite um valor de 0 a 10: "))

match opcao:
    case 1:
        print("Voce escolheu o 1!")
    case 2:
        print("Voce escolheu o 2!")
    case 3:
        print("Voce escolheu o 3!")
    case 4:
        print("Voce escolheu o 4!")