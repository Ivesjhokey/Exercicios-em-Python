'''Adapte o código do desafio 107, criando uma função adicional
   chamada moeda() que consiga mostrar os valores como um valor
   monetário formatado.'''

from exercicios.ex108 import Moeda2

n1 = float(input('digite o preço R$: '))
print(f'Aumentando 10% de {Moeda2.moeda(n1)} temos {Moeda2.moeda(Moeda2.aumentar(n1, 10))}')
print(f'Diminuindo 10% de {Moeda2.moeda(n1)} temos {Moeda2.moeda(Moeda2.diminuir(n1, 10))}')
print(f'A metade de {Moeda2.moeda(n1)} = {Moeda2.moeda(Moeda2.metade(n1))}')
print(f'O dobro de {Moeda2.moeda(n1)} = {Moeda2.moeda(Moeda2.dobro(n1))}')
