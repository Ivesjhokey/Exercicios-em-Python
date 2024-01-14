'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
   No final, mostre uma listagem de preços, organizando os dados em forma tabular'''

listagem = ('lapis', 1.00, 'caneta', 2.00, 'borracha', 3.00)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<20} R${listagem[c+1]}')
