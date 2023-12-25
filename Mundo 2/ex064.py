# alternativa 1 de jhokey

parar = False
soma = 0
somanum = 0
while not parar:
    n1 = int(input('digite um numero para somar [999] para parar: '))
    if n1 != 999:
        soma = soma + n1
        somanum += 1
    else:
        parar = True
print('voce digitou {} numeros e a soma entre eles e {}'.format(somanum,soma))
