preço = float(input('digite o preço do produto: '))
desc = ((preço/100) * 5)
final = preço - desc
print('o valor do produto foi {}$, com o desconto de 5% = {}$, passara a custar {}$'.format(preço, desc, final))
