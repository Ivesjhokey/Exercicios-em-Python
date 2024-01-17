"""Crie um módulo chamado modulos.py que tenha as funções incorporadas
   aumentar(), diminuir(), dobro() e metade(). Faça também um programa
   que importe esse módulo e use algumas dessas funções."""


# import Moeda5 ou

from ex107 import Moeda
n1 = float(input('digite o preço R$: '))
print(f'aumentando 10% de {n1} temos {Moeda.aumentar(n1, 10)}')
print(f'diminuindo 10% de {n1} temos {Moeda.diminuir(n1, 10)}')
print(f'o dobro de {n1} = {Moeda.dobro(n1)}')
print(f'a metade de {n1} = {Moeda.metade(n1)}')


'''outro metodo:
from Moeda5 import aumentar, diminuir, dobro, metade
n1 = float(input('digite o preço R$: '))
print(f'aumentando 10% de {n1} temos {aumentar(n1, 10)}')
print(f'diminuindo 10% de {n1} temos {diminuir(n1, 10)}')
print(f'o dobro de {n1} = {dobro(n1)}')
print(f'a metade de {n1} = {metade(n1)}')'''
