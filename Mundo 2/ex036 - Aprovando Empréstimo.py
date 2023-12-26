'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
   Pergunte o valor da casa, o salario do comprador, e em quantos anos ele vai pagar.
   A prestação mensal, não pode exceder 30% do salario ou então o empréstimo será negado'''

casa = float(input('qual o valor da casa? '))
salario = float(input('qual o valor do seu salario? '))
parcelar = int(input('em quantos anos ira parcelar? '))

if (casa / (parcelar * 12)) > (salario / 100) * 30:
    print('a parcela mensal nao pode exceder 30% do seu salario mensal')
else:
    print('se parcelar {} em {} ano(s), voce ira pagar {} por mes'.format(casa, parcelar, casa / (parcelar * 12)))
