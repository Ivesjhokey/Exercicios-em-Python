listagem = ('lapis', 1.00, 'caneta', 2.00, 'camisinha', 3.00)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<20} {listagem[c+1]} R$')
