# alternativa 1 de jhokey

soma = 0
somanum = 0
while True:
    n1 = int(input('digite um numero para somar [999] para parar: '))
    if n1 == 999:
        break
    soma = soma + n1
    somanum += 1
print('voce digitou {} numeros e a soma entre eles e {}'.format(somanum, soma))
