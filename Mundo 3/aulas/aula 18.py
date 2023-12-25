"""dados = []
dados.append('pedro')
dados.append(25)
print(dados[0])
print(dados[1])
print(dados)

print('\n')

# pessoas = [['maria', 19], ['joao', 32], dados[:]] daria para inserir a lista assim tambem
pessoas = [['maria', 19], ['joao', 32]]
pessoas.append(dados[:])
print(pessoas)
print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[0])

print('\n')

#outra maneira de declarar listas é:

galera = [['joao', 19], ['ana', 33], ['ives', 22], ['samu', 21]]

for p in galera:
    #print(p)
    #print(p[0])
    #print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade')"""

galera = []
dados = []
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('digite um nome? ')))
    dados.append(int(input('digite a idade? ')))
    galera.append(dados[:])
    dados.clear()

for c in galera:
    if c[1] >= 21:
        print(f'{c[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{c[0]} é menor de idade')
        totmen += 1

print(galera)
print(dados)
print(totmai)
print(totmen)

