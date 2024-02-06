# Vá na pasta modelos, pegue o arquivo restaurante e importe a classe Restaurante
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca','Gourmet')

restaurante_praca.receber_avaliacao('Popo',10)
restaurante_praca.receber_avaliacao('Teto',8)
restaurante_praca.receber_avaliacao('Carlinha',5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()