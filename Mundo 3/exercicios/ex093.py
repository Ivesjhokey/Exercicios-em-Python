dicionario = dict()
dicionario['nome'] = str(input('nome do jogador: '))
n2 = int(input(f'quantas partidas jogou {dicionario["nome"]}: '))
gols = []
total = 0
for c in range(0, n2):
    n1 = int(input(f'quantos gols na partida {c+1}?: '))
    gols.append(n1)
    total = total + n1
dicionario['gols'] = gols
dicionario['total'] = total
print(dicionario)
print()
for c, v in dicionario.items():
    print(f'o campo {c} tem o valor {v}')
print()
print(f'o jogador {dicionario["nome"]} jogou {n2} partidas')
for c, v in enumerate(gols):
    print(f'na partida {c+1} fez {v} gols')
print(f'com um total de {total} gols')