'''Crie um programa onde 4 jogadores joguem um dado e tenhão
   resultados aleatórios. Guarde esses resultados em um dicionário.
   No final, Coloque esse dicionário em ordem, sabendo que o vencedor
   tirou o maior o maior número no dado.'''

from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = {}
for c, v in jogo.items():
    print(f'{c} tirou {v}')
ranking = sorted(jogo.items(), reverse=True, key=itemgetter(1))
for c, v in enumerate(ranking):
    print(f'{c+1} lugar é o {v[0]} que tirou {v[1]} no dado')
