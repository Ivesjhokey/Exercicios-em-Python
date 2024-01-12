"""Modifique as funções que foram criadas no desafio 107 para que elas
   aceitem um parâmetro a mais, informando se o valor retornado por elas
   vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""


from exercicios.ex109 import Moeda3

n1 = float(input('digite o preço R$: '))
print(f'Aumentando 10% de {Moeda3.moeda(n1)} temos {Moeda3.aumentar(n1, 10, True)}')
print(f'Diminuindo 10% de {Moeda3.moeda(n1)} temos {Moeda3.diminuir(n1, 10, True)}')
print(f'A metade de {Moeda3.moeda(n1)} = {Moeda3.metade(n1, True)}')
print(f'O dobro de {Moeda3.moeda(n1)} = {Moeda3.dobro(n1, True)}')
