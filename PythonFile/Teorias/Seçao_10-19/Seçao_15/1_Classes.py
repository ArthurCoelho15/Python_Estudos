"""

Em Programação Orientada a Objetos:

CLASSES:
    1. [1] São objetos do mundo real representados digitalmente
        Ex: Um sistema para automatizar o controle de lâmpadas da casa

    2. Sintaxe:
        - Para definirmos uma classe, utilizamos a palavra reservada 'class'.
        - Quando nomeamos nossas classes em Python utilizamos a inicial maiúscula. Caso o nome seja composto, ambas as palavras com inicial
        maiúscula e juntas (CamelCase).
            - Ex: LampadaSala

    3. As classes devem conter:


        [1] Atributos:
            - Representam as características do objeto. No caso da lâmpada, possivelmente iríamos querer saber se é 110V ou 220V,
        se é branca, amarela ou RGB, qual a luminosidade, se está ligada ou desligada, etc.
            - Por convenção, em Python, todo atributo de uma classe é público, caso queiramos demostrar que um atributo é privado utilizamos
        o duplo under (__), também chamado de MangLing.
            (1) Atributos de Instância:
                -> São atributos declarados dentro do método construtor, cada instância/objeto tem seu valor.
                    - Método construtor é um método especial utilizado para a construção do objeto.
                        Métodos construtores (Sintaxe) -> def __init__(self, argumento1, argumento2, etc):

            (2) Atributos de Classe / Atributos estáticos:
                -> São atributos declarados fora do método construtor, o valor é compartilhado para todas as instâncias/objetos.
            (3) Atributos Dinâmicos (menos comum):
                -> São atributos que declaramos fora da classe
                    - Podemos adicionar atributos;
                    - Podemos excluir atributos.



        [2] Métodos (funções):
            - Representam o comportamento do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema. No caso da lâmpada,
        um comportamento comum seria de ligar e desligar a lâmpada, no caso de uma lâmpada RGB iriamos querer mudar a cor, etc.
            (1) Métodos de instância;
                -> Utiliza o parâmetro 'self', nos referimos as instâncias.
            (2) Métodos de classe;
                -> Utiliza o parametro 'cls' (classe), nos referimos a classe.
                -> Sintaxe:
                    @classmethod
                    def nome_da_funcao(cls):
                        // funcao
            (3) Métodos estáticos.
                -> Não utiliza parâmetros.
                -> Sintaxe:
                    @staticmethod
                    def nome_da_funcao():
                        // funcao


        [3] Entidades:
            - Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos esses objetos
        que serão mapeados para classes de entidades.
"""

#1 / #2 CLASSES:

"""
class Lampada:
    pass

lamp = Lampada()
print(type(lamp))
"""

#3 CONTEUDO DAS CLASSES:


# Atributos [1]:

"""
# Atributos de instância (1):
class Lampada2:

    # Construindo a classe com o construtor (metodo):
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem # Atributo público
        self.__cor = cor # Atributo privado
        self.ligada = False
        
lampada_classe = Lampada2(220,'RGB')

print(type(lampada_classe))
print(lampada_classe.voltagem)
print(lampada_classe.cor) # NOK, AttributeError, elemento privado
print(lampada_classe._Lampada2__cor) # Fazemos dessa forma para acessar um elemento privado (MangLing)
print(lampada_classe.ligada)
"""
"""
# Atributos de classe (2):
class Produto:

    imposto = 1.05 # atributo de classe, utilizando imposto (ex. ICMS)
    contador = 0 # criamos o contador de id

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1 # atribuimos o valor 1 para o primeiro produto a ser chamado
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id # depois que o primeiro prod ganha o valor a função atualiza para incrementar 1 e atualizar o prox prod

prod1 = Produto('PS4', 'Video-game', 4500)
prod2 = Produto('PC', 'Desktop', 6200)
prod3 = Produto('Xbox', 'Video-game', 4130)
"""
"""
print(f'O {prod1.nome} está na sessão de {prod1.descricao} e custa {prod1.valor}')
print(f'O valor do imposto é de {round((Produto.imposto - 1) * 100)}%')
print(f'O id do {prod1.nome} é {prod1.id}')
print(f'O id do {prod2.nome} é {prod2.id}')
"""
"""
# __dict__ é a forma que utilizamos para ver todos os atributos do objeto
print(prod1.__dict__)

# Adicionando atributos:
prod1.peso = '500g'

print(f'O peso do {prod1.nome} é {prod1.peso}')
print(prod1.__dict__)

# Excluindo atributos:
del prod1.valor
del prod1.descricao

#print(f'O valor do {prod1.nome} é {prod1.valor}') # AttributeError, atributo não existe mais
#print(f'O valor do {prod1.descricao} é {prod1.descricao}') # AttributeError, atributo não existe mais
print(prod1.__dict__)
"""


# Métodos [2]:

"""
# Biblioteca para encriptar senhas
from passlib.hash import pbkdf2_sha256 as crypt


class Usuario:

    contador = 0

    # Definindo um class method, não tem a instância self, portanto se refere a classe, não a instância.
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuario(s) no sistema')

    # Definindo um static method, não tem parametro, não se refere a instância e nem a classe.
    @staticmethod
    def definicao():
        print('Abububle')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__email = email.lower()
        self.__senha = crypt.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if crypt.verify(senha, self.__senha):
            return True
        return False

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
email = input('Digite seu email: ')
senha = input('Digite seu senha: ')
confirma_senha = input('Digite novamente sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('As senhas não coincidem, finalizando o programa...')
    exit(1)

print('Usuario criado com sucesso!!!')

senha = input('Digite sua senha para entrar: ')

if user.checa_senha(senha):
    print(f'Acesso permitido, {user.nome_completo()}')
else:
    print('Acesso negado')

# Como criptografamos a senha, não conseguimos vê-la
print(f'A senha do usuário criptografada é: {user._Usuario__senha}')
print(user.__dict__)
"""