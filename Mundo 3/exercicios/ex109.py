"""para que elas aceitem um parâmetro a mais
informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
desenvolvida no desafio 108."""


import modulos
n1 = float(input('digite o preço R$: '))
n2 = str(input('quer converter "." para ","? [sim],[nao]: ')).lower()

print(f'aumentando 10% de {modulos.moeda(n1, n2)} temos {modulos.moeda(modulos.aumentar(n1), n2)}')
print(f'diminuindo 10% de {modulos.moeda(n1, n2)} temos {modulos.moeda(modulos.diminuir(n1), n2)}')
print(f'a metade de {modulos.moeda(n1, n2)} = {modulos.moeda(modulos.metade(n1), n2)}')
