class Livro:

    def __init__(self, titulo, autor, ano_publicacao, disponivel=True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = disponivel

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} - {self._disponivel}'

    def emprestar(self):
        self._disponivel = False


livro1 = Livro('Os tres porquinhos', 'Joseph Jacobs',1853)
livro2 = Livro('Mindset', 'Carol S. Dweck',2017)

livro1.emprestar()

print(livro1)
print(livro2)
