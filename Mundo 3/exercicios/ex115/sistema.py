'''Crie um pequeno sistema modularizado que permita cadastrar
   pessoas pelo seu nome e idade em um arquivo de texto simples.
   O sistema só vai ter 2 opções: cadastrar uma nova pessoa e 
   listar todas as pessoas cadastradas.'''


from mundo3final.lib.interface import *
from mundo3final.lib.arquivo import *

arquivo = 'pessoas.txt'

if not arquivoexiste(arquivo):
    criararquivo(arquivo)


while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerarquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leiaint('idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('\033[32mSaindo do sistema... ate logo!\033[m')
        break
    else:
        print('\033[31mERRO, digite uma opção valida\033[m')
