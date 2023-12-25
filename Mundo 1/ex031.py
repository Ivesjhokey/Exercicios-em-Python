n1 = float(input('digite a distancia da viagem em km: '))
if n1 > 200:
    print('a sua viagem custara {}'.format(n1*0.45))
else:
    print('a sua viagem custara {}'.format(n1*0.50))

preço = (n1 * 0.45) if n1 > 200 else (n1 * 0.50) #if simplificado
print(preço)
