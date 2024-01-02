'''Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
   Depois disso, você deve mostrar, para cada palavra, quais sâo as suas vogais.'''

#alternativa jhokey
palavras = ('hamburguer', 'suco', 'pudim', 'tetas')
for c in palavras:
    print(f'em {c} temos', end=' ')
    for letras in c:
        if letras in 'aeiou':
            print(letras, end=' ')
    print()

#alternativa guanabara
palavras = ('hamburguer', 'suco', 'pudim', 'tetas')
for c in palavras:
    print(f'\nem {c} temos', end=' ')
    for letras in c:
        if letras in 'aeiou':
            print(letras, end=' ')
