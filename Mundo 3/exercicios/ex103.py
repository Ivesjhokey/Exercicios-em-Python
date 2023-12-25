# Faça um programa que tenha uma função chamada ficha()
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(a='', b=''):
    return f'o jogador {a} marcou {b} gols'


nome = str(input('nome: '))
if nome == '':
    nome = 'desconhecido'

gols = str(input('gols: '))
if gols == '':
    gols = 'x'

n1 = ficha(a=nome, b=gols)
print(n1)


"""# alternativa guanabara


def ficha(jog='<desconhecido>', gol=0):
    print(f'o {jog} fez {gol} gols no campeonato')


n = str(input('nome: '))
g = str(input('gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)"""