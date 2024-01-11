"""Modifique as funções que foram criadas no desafio 107 para que elas
   aceitem um parâmetro a mais, informando se o valor retornado por elas
   vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""


import Moedars
n1 = float(input('digite o preço R$: '))
n2 = str(input('quer converter "." para ","? [sim],[nao]: ')).lower()

print(f'aumentando 10% de {Moedars.moeda(n1, n2)} temos {Moedars.aumentar(n1, n2)}')
print(f'diminuindo 10% de {Moedars.moeda(n1, n2)} temos {Moedars.diminuir(n1, n2)}')
print(f'a metade de {Moedars.moeda(n1, n2)} = {Moedars.metade(n1, n2)}')
