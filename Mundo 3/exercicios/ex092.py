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