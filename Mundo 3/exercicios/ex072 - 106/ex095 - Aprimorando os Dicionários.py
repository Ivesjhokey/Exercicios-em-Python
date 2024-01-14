'''Aprimore o DESAFIO 093 para que ele funcione com vários
   jogadores, incluindo um sistema de visualização de detalhes
   do aproveitamento de cada jogador'''

time = []
jogador = {}
while True:
    jogador['nome'] = str(input('nome do jogador: '))
    n2 = int(input(f'quantas partidas jogou {jogador["nome"]}: '))
    gols = []
    total = 0

    for c in range(0, n2):
        n1 = int(input(f'quantos gols na partida {c+1}?: '))
        gols.append(n1)
        total = total + n1

    jogador['gols'] = gols
    jogador['total'] = total
    time.append(jogador.copy())

    resp = str(input('quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

for c in jogador.keys():            # jogador.keys ira contar apenas os valores de chaves dos dicionarios
    print(f'{c:<20}', end='')       # aqui vai mostrar as chaves pulando de 15 em 15
print()

# primeira tentativa para mostrar os valores das chaves
for indice, dicionario in enumerate(time):
    print(f'{indice}', end=' = ')
    print(f'{str(dicionario["nome"]):<16}', end='')
    print(f'{str(dicionario["gols"]):<16}', end='')
    print(f'{str(dicionario["total"]):>7}')

"""# segunda tentativa para mostrar os valores das chaves mas e foda pq o indice caga na ordem bonitinha
#so fica bom se tirar o indice, ai fica file, porem nao mostra o numero dele na lista

for indice, dicionario in enumerate(time):
    print(indice, '=', end=' ')
    for keys, valor in dicionario.items():
        print(f'{str(valor):<15}', end='')
    print()"""


print()
while True:
    busca = int(input('mostar dados de qual jogador? (999) para parar: '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'nao existe jogador com codigo {busca}')
    else:
        print(f'levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'no jogo {i+1} fez {g} gols')
print('fim do programa')




"""# alternativa guanabara
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('nome do jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'quantos gols na partida {c+1}?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('erro, responda apenas com [S/N]')
    if resp == 'N':
        break

print('-=' * 40)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('mostar dados de qual jogador? (999) para parar: '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'nao existe jogador com codigo {busca}')
    else:
        print(f'levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   no jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<<VOLTE SEMPRE>>')"""
