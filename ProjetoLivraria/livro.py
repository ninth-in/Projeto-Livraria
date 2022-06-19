from db.database import Graph
class Livro(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.204.254.83:7687', user='neo4j', password='bed-secret-pulse')

    def cadastrarLivro(self, titulo, autor, genero):
        self.db.execute_query('CREATE (l:Livro {titulo:$titulo, autor:$autor, genero:$genero})',
        {'titulo': titulo, 'autor': autor, 'genero': genero})
        return 1

    def atualizarDados(self, titulo, newAutor, newGenero):
        self.db.execute_query('MATCH (l:Livro {titulo:$titulo}) SET l.autor = $autor, l.genero = $genero',
        {'titulo': titulo, 'autor': newAutor, 'genero': newGenero})
        return 1

    def deletarLivro(self, titulo):
        self.db.execute_query('MATCH (l:Livro {titulo:$titulo}) DETACH DELETE l',
        {'titulo': titulo})
        return 1

    def listarLivros(self):
        return self.db.execute_query('MATCH (l:Livro) RETURN l')

    def buscarTitulo(self, titulo):
        return self.db.execute_query('MATCH (l:Livro {titulo:$titulo}) RETURN l',
                                     {'titulo': titulo})
    def buscarGenero(self, genero):
        return self.db.execute_query('MATCH (l:Livro {genero:$genero}) RETURN l',
                                     {'genero': genero})