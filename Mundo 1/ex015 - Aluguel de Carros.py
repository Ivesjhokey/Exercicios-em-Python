'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
   Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado'''

km = float(input('digite quantos km rodados: '))
dias = float(input('digite quantos dias foi usado: '))
pago = (km * 0.15) + (dias * 60)
print('o total a pagar é {}$'.format(pago))
