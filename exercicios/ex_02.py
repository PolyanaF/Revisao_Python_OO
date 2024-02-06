# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo,
# cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.


class Carro:

    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'Modelo = {self.modelo} | Cor = {self.cor} | Ano = {self.ano}'

    def listar_carros():
        for carro in Carro.carros:
            print(f'Modelo = {carro.modelo} | Cor = {carro.cor} | Ano = {carro.ano}')

carro1 = Carro('Corsinha','Preto',2002)
carro2 = Carro('Astra','Prata', 2012)
carro3 = Carro('Cherry QQ','Vermelho',2008)

Carro.listar_carros()

# Crie uma classe chamada Restaurante com os atributos nome, categoria,
# ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:

    # LISTA
    restaurantes = []

    def __init__(self, nome, categoria, ano_criacao, responsavel, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ano_criacao = ano_criacao
        self.responsavel = responsavel
        self.ativo = ativo

        # AQUI ESTAMOS ADICIONANDO O NOVO RESTAURANTE NA LISTA
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ano_criacao} | {self.responsavel}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.ano_criacao} | {restaurante.responsavel}')

restaurante_praca = Restaurante('Praça','Italiana',2020,'Polyana')
restaurante_pizza = Restaurante('Pizza Place','Fast Food',2014,'Matheus')

Restaurante.listar_restaurantes()

# 5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos
# desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:

    clientes = []

    def __init__(self, nome, idade, nacionalidade, genero = 'Indefinido'):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.genero = genero
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.nacionalidade} | {self.genero}'

    def listar_cliente():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.idade} | {cliente.nacionalidade} | {cliente.genero}')

cliente1 = Cliente('Matheus', 24, 'Arabe', 'Masculino')
cliente2 = Cliente('Polyana', 23, 'Brasileira', 'Feminino')
cliente3 = Cliente('Carlos', 21, 'Brasileiro')

Cliente.listar_cliente()

# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um
# método especial __str__ para imprimir uma representação em string da pessoa. Implemente também
# um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação
# personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.profissao } - {self.idade} anos'

    def aumentar_idade(self, aniversario=1):
        self.idade += aniversario

    def saudacao(self):
        print(f'Olá {self.profissao} {self.nome}!')

pessoa1 = Pessoa('Polyana',23,'Engenheira')

print(pessoa1)

pessoa1.aumentar_idade()

print(pessoa1)

pessoa1.saudacao()



