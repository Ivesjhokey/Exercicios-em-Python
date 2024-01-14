"""Faça um mini-sistema que utilize o Interactive Help do Python.
   O usuário vai digitar o comando e o manual vai aparecer.
   Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
   OBS: use cores."""


cor = ('\033[m',            # vazio
       '\033[7:30:41m',     # vermelho
       '\033[30:42m',       # verde
       '\033[30:43m',       # amarelo
       '\033[30:44m',)      # azul


def ajuda(n2):
    return print(cor[4], '-' * 30),\
        print('SISTEMA DE AJUDA PYHELP'),\
        print('-' * 30),\
        print(cor[0]),\
        print(cor[2]),\
        print(help(n2)),\
        print(cor[0])


while True:
    n1 = str(input(f'{cor[1]} função ou biblioteca: {cor[0]}'))
    if n1 == 'fim'.lower():
        break
    else:
        n3 = ajuda(n1)
