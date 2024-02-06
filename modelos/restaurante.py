from modelos.avaliacao import Avaliacao

class Restaurante:
    ''' SELF é a referencia da instancia atual que estamos utilizando no momento
    É comum encontrar como THIS, ao inves de SELF tambem

    __init__ O 'init' é um método utilizado como construtor da classe.
    Ele é chamado toda vez que você cria um objeto.

    __str__ serve para que a gente receba os atributos em formato de texto

    '''

    # Lista
    restaurantes = []

    def __init__(self, nome, categoria, ativo=False):
        self._nome = nome.title() # O .title() deixa a primeira letra maiuscula
        self._categoria = categoria.upper() # O .upper() deixa tudo maiusculo

        # Quando colocamos um " _ " antes do atributo tornamos ele privado,
        # não esperamos que o usario mude o valor dele
        self._ativo = ativo

        self._avaliacao = []

        # O .append() adiciono na lista
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    # Uma boa prática sempre que temos um metodo não referenciado como um objeto/instancia
    # E sim um metodo refrenciado a classe, precisamos indicar que é
    # um "metodo da classe" ( @classmethod) e sempre que temos um  @classmethod e estamos
    # utilizando informações referente a esse metodo podemos colocar como argumento
    # o "cls" (é uma convenção)
    @classmethod
    def listar_restaurantes(cls):

        # Colocamos o titulo entre chaves para poder definir o espaço das casas
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Media".ljust(25)} | {"Status"}')

        # E ao inves de chamarmos a classe para poder chamar a lista "restaurante" utilizamos
        # o cls, para consegui8r indicar que se trata de um metodo da classe
        for restaurante in cls.restaurantes:
            # Com o " ljust " definimos o numero de casas que o valor ira ficar
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    # Sempre que utilizamos a palavra "property", queremos modificar como o atributo será lida
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):

    # Se não tiver avaliações
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media









