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
