'''Crie um programa que leia o nome, ano de nascimento e carteira de trabalho
   e cadastre-os(com idade) em um dicionário, se por acaso a CTPS for diferente
   de ZERO, o dicionario receberá também o ano de contratação e o salário.
   Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

dicionario = dict()
dicionario['nome'] = str(input('nome: '))
n1 = int(input('ano de nascimento: '))
dicionario['idade'] = datetime.now().year - n1
dicionario['ctps'] = int(input('carteira de trabalho [0 = nao tem]: '))

if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('ano de contratação: '))
    dicionario['salario'] = float(input('salario: '))
    dicionario['aposentadoria'] = dicionario['idade'] + dicionario['contratação'] + 35 - datetime.now().year

for c, v in dicionario.items():
    print(c, '=', v)
