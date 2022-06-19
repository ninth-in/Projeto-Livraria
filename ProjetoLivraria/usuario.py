from db.database import Graph
class Usuario(object):
    def __init__(self):
        self.db = Graph(uri='link', user='neo4j', password='senha')

    def cadastrarUsuario(self, nome, idade, email, login, senha):
        self.db.execute_query('CREATE (u:Usuario {nome:$nome, idade:$idade, email:$email, login:$login, senha:$senha})',
        {'nome': nome, 'idade': idade, 'email': email, 'login':login, 'senha': senha})
        return 1

    def atualizarDados(self, nome, newEmail):
        self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.email = $email',
        {'nome': nome, 'email': newEmail})
        return 1

    def deletarUsuario(self, login):
        self.db.execute_query('MATCH (u:Usuario {login:$login}) DETACH DELETE u',
        {'login': login})
        return 1

    def livrosAlugados(self, login):
        return self.db.execute_query('MATCH (u:Usuario {login:$login})-[r:ALUGOU{devolucao: $devolucao}]->(l:Livro) RETURN l.titulo',
                                     {'login': login,'devolucao':False})

    def totalEmprestimo(self,login):
        return self.db.execute_query('MATCH (u:Usuario {login:$login})-[r:ALUGOU]->(l:Livro) RETURN COUNT(l)',
                                     {'login': login})

    def alugarLivro(self, titulo, login):
        return self.db.execute_query('MATCH (u:Usuario {login:$login}), (l:Livro {titulo:$titulo}) CREATE (u)-[r:ALUGOU{devolucao: $devolucao}]->(l) RETURN l',
                                     {'login': login, 'titulo': titulo, 'devolucao': False})
        

    def devolverLivro(self, titulo, login):
        self.db.execute_query('MATCH (u:Usuario {login:$login})-[r:ALUGOU]->(l:Livro {titulo:$titulo}) SET r.devolucao = $devolucao',
                                     {'titulo': titulo, 'login': login,'devolucao': True})
        return 1

    def verificarCadastro(self, login):
        return self.db.execute_query('MATCH (u:Usuario {login:$login}) RETURN u.login, u.senha',
        {'login': login})