carrinho = 0
mmil = 0
nbarato = ''
pbarato = 0
while True:
    n1 = input('digite o nome do produto: ')
    n2 = float(input('digite seu preço: '))
    carrinho = carrinho + n2
    if pbarato == 0:
        pbarato = n2
        nbarato = n1
    elif n2 < pbarato:
        pbarato = n2
        nbarato = n1
    if n2 > 1000:
        mmil += 1
    n3 = input('quer continuar?[S/N]: ').lower()
    if n3 == 'n':
        break
print(f'o total da compra foi R$ {carrinho:.2f}\n'
      f'temos {mmil} produtos custando mais de R$ 1.000\n'
      f'o produto mais barato foi {nbarato} que custa R$ {pbarato}')
