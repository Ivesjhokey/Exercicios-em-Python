palavras = ('hamburguer', 'suco', 'pudim', 'tetas')
for c in palavras:
    print(f'em {c} temos', end=' ')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()



