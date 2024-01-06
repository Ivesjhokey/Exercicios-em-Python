'''Faça um programa que tenha uma função chamada maior(), que
   receba vários parâmetros com valores inteiros. Seu programa
   tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(lista):
    print(f'dos valores {lista}\no maior é {max(lista)}')


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior(numeros)


"""def maior(*valor):
    print(f'os numeros foram:', end=' ')
    for c in valor:
        print(c, end=' ')
    print()
    print(f'e o maior numero é {max(*valor)}')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"""
