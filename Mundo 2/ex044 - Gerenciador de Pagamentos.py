'''Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
   - A vista dinheiro/cheque = 10% de desconto
   - A vista no cartão = 5% de desconto
   - Em até 2x no cartão = preço normal
   - Em 3x ou mais no cartão = 20% de juros'''

pag = float(input('digite o valor do produto: '))
con = input('escolha a condição de pagamento?\ndinheiro a vista,(10%) de desconto,\ncredito a vista,'
            '(5%) de desconto\n2 parcelas(valor normal),\n3 parcelas ou mais(20% de juros)\n')
if con == 'dinheiro a vista':
    print('o valor a ser pago sera:', pag - ((pag / 100) * 10))
elif con == 'credito a vista':
    print('o valor a ser pago sera:', pag - ((pag / 100) * 5))
elif con == '2 parcelas':
    print('o valor a ser pago sera:', pag)
elif con == '3 parcelas ou mais':
    print('o valor a ser pago sera:', pag + ((pag / 100) * 20))
