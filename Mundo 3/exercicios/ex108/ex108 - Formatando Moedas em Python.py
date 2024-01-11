'''Adapte o código do desafio 107, criando uma função adicional
   chamada moeda() que consiga mostrar os valores como um valor
   monetário formatado.'''

import Moedar

n1 = float(input('digite o preço R$: '))
print(f'aumentando 10% de {Moedar.moeda(n1)} temos {Moedar.aumentar(n1)}')
print(f'diminuindo 10% de {Moedar.moeda(n1)} temos {Moedar.diminuir(n1)}')
print(f'a metade de {Moedar.moeda(n1)} = {Moedar.metade(n1)}')
