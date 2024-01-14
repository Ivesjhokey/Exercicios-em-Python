'''Faça um programa que tenha uma lista chamada números e duas funções
   chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
   e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
   entre todos os valores PARES sorteados pela função anterior.'''

from random import randint
numeros = list()
def sorteia(lista):
    print('sorteando 5 valores: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(lista[c], end=' ')
    print()


def somapar(lista):
    print(f'somando os valores pares de: ', end='')
    contador = 0
    for c in range(0, 5):
        print(lista[c], end=' ')
        if lista[c] % 2 == 0:
            contador = contador + lista[c]

    print(f'temos {contador}')

sorteia(numeros)
somapar(numeros)
