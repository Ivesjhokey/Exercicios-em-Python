from ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro na criação do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'Houve um ERRO na abertura do arquivo {arquivo}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('erro ao cadastrar nova pessoa')
        else:
            print(f'novo registro de {nome} adicionado.')
            a.close()
