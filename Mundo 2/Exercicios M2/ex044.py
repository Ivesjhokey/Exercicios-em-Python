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
