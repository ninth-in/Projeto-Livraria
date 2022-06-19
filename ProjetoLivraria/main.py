from livro import Livro
from usuario import Usuario
from helper.write_a_json import write_a_json as wj
import json

l = Livro()
u = Usuario()

while 1:
    print("------------BEM-VINDO A LIVRARIA------------")    
    option = input('1. Entrar\n2. Cadastrar usuario\n3. Gerenciar Livros\n4. Sair\n--------------------------------------------\n')
    
    if option == '1':
            print("------------LOGIN------------")  
            login = input('Login:')
            senha = input('Senha:')
            r = u.verificarCadastro(login)
            if ((r[0]['u.login']) == login) and ((r[0]['u.senha']) == senha):
                #entra no menu principal
                while 1:
                    print("------------MENU PRINCIPAL------------")
                    menu1 = input('1. Alugar Livro\n2. Devolver Livro\n3. Listar Livros\n4. Buscar livro por titulo\n5. Buscar livro por genero\n6. Perfil do Usuario\n0. Sair\n--------------------------------------\n')

                    if menu1 == '1':
                        titulo = input('Titulo para alugar: ')
                        r = u.alugarLivro(titulo, login)
                        if r == []:
                            print("Livro não existe!")
                        else:
                            print("Emprestimo realizado com sucesso!")

                    if menu1 == '2':
                        titulo = input('Titulo para devolver: ')
                        r = u.devolverLivro(titulo,login)
                        if r == 1:
                            print("Livro devolvido!")

                    if menu1 == '3':
                        r = l.listarLivros()
                        if r != []:
                            wj(r,"ListaLivros")
                            with open(f'./json/ListaLivros.json', encoding='utf-8') as meu_file:
                                meu_json = json.load(meu_file)
                            for i in meu_json:
                                print('Livro: ',i['l']['titulo'],' Autor: ',i['l']['autor'],' Genero: ',i['l']['genero'])
                        else:
                            print('Livraria em reforma! Logo voltaremos!')

                    if menu1 == '4':
                        titulo = input('Titulo: ')
                        r = l.buscarTitulo(titulo)
                        if r != []:
                            wj(r,"ListaTitulo")
                            with open(f'./json/ListaTitulo.json', encoding='utf-8') as meu_file:
                                meu_json = json.load(meu_file)
                            for i in meu_json:
                                print('Livro: ',i['l']['titulo'],' Autor: ',i['l']['autor'],' Genero: ',i['l']['genero'])
                        else:
                            print('Livro não existe!')

                    if menu1 == '5':
                        genero = input('Genero: ')
                        r = l.buscarGenero(genero)
                        if r != []:
                            wj(r,"ListaGenero")
                            with open(f'./json/ListaGenero.json', encoding='utf-8') as meu_file:
                                meu_json = json.load(meu_file)
                            for i in meu_json:
                                print('Livro: ',i['l']['titulo'],' Autor: ',i['l']['autor'])
                        else:
                            print('Sem livros :(')

                    if menu1 == '6':
                        print('---------PERFIL---------')
                        perfil = input('1. Livros alugados\n2. Atualizar e-mail\n3. Deletar Usuario\n4. Total de Emprestimos\n5. Sair\n------------------------\n')
                        if perfil == '1':
                            r = u.livrosAlugados(login)
                            if r != []:
                                wj(r,"LivrosAlugados")
                                with open(f'./json/LivrosAlugados.json', encoding='utf-8') as meu_file:
                                    meu_json = json.load(meu_file)
                                for i in meu_json:
                                    print('Livro: ',i['l.titulo'])
                            else:
                                print('Sem livros alugados no momento!')
                        elif perfil == '2':
                            newEmail = input('Novo email:')
                            u.atualizarDados(login, newEmail)
                            if r == 1:
                                print('E-mail atualizado com sucesso!')
                        elif perfil == '3':
                            r = u.deletarUsuario(login)
                            if r == 1:
                                print('Usuario deletado com sucesso!')
                        elif perfil == '4':
                            r = u.totalEmprestimo(login)
                            print('Total de Emprestimos de Livro: ', r[0]['COUNT(l)'])

                    if menu1 == '0':
                        break
            else:
                print('Email ou senha inválido! Tente novamente!')

    elif option == '2':
        nome = input('Entre com seu nome: ')
        idade = input('Entre com sua idade: ')
        email = input('Entre com seu email: ')
        login = input('Entre com seu login: ')
        senha = input('Entre com sua senha: ')
        r = u.cadastrarUsuario(nome, idade, email, login, senha)
        if r == 1:
            print('Usuario cadastrado com sucesso!')

    elif option == '3':
        while 1:
            print('------Gerenciamento de livros------')
            aux = input('1. Cadastrar Livro\n2. Atualizar dados de um livro\n3. Deletar livro\n0. Sair\n--------------------------------\n')
            if aux == '1':
                titulo = input('Titulo:')
                autor = input('Autor:')
                genero = input('Genero:')
                l.cadastrarLivro(titulo, autor, genero)
            
            elif aux == '2':
                titulo = input('Titulo:')
                newAutor = input('Novo autor:')
                newGenero = input('Novo genero:')
                l.atualizarDados(titulo, newAutor, newGenero)
            
            elif aux == '3':
                titulo = input('Titulo:')
                l.deletarLivro(titulo)
            
            elif aux == '0':
                break

            else:
                break
    else:
        break

l.db.close()
u.db.close()