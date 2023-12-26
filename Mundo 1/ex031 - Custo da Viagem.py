'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
   Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas'''

n1 = float(input('digite a distancia da viagem em km: '))
if n1 > 200:
    print('a sua viagem custara {}'.format(n1*0.45))
else:
    print('a sua viagem custara {}'.format(n1*0.50))

preço = (n1 * 0.45) if n1 > 200 else (n1 * 0.50) #if simplificado
print(preço)
