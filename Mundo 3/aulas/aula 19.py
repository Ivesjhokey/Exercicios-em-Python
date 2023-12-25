"""pessoas = {'nome': 'ives', 'sexo': 'masculino', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])

print(f'{pessoas["nome"]} do sexo {pessoas["sexo"]} tem {pessoas["idade"]} anos')
print(f"{pessoas['nome']} do sexo {pessoas['sexo']} tem {pessoas['idade']} anos")
# para fazer funcionar devemos utilizar aspas duplas na hora de referenciar ou mudar o print para aspas duplas
# e referenciar com aspas simples

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas:
    print(k)

for k in pessoas:
    print(pessoas)

for k, v in pessoas.items():         # um for para mostrar dois contadores
    print(k, v)

del pessoas['sexo']                 # forma de deletar uma chave com seu respectivo valor
print(pessoas)

pessoas['nome'] = 'samu'            # forma de substituir um valor dentro de uma chave
print(pessoas)

pessoas['mulher'] = 'beatriz'     # forma de adicionar coisas no dicionario
print(pessoas)"""

"""# criando dicionario dentro de lista

brasil = []
estado1 = {'uf': 'parana', 'sigla': 'PR'}
estado2 = {'uf': 'santa catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])

print(brasil[0]['uf'])
print(brasil[1]['sigla'])"""

# papara papara papara clack bum

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('qual estado? '))
    estado['sigla'] = str(input('qual sigla? '))
    brasil.append(estado.copy())    # nao podemos usar copia com fatiamento [:] pois nao pode mesmo, seila kkk
print(brasil)
print(estado)
print()

for e in brasil:                    # aqui mostra o que tem dentro dos indices
    print(e)
print()

for e in brasil:
    for k, v in e.items():          # aqui me mostra as chaves e seus valores
        print(k, v)
print()

for e in brasil:
    for k, v in e.items():       # aqui me mostra as chaves
        print(k)
print()

for e in brasil:
    for k, v in e.items():
        print(v)                 # aqui me mostra os valores
