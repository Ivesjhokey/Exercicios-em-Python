'''Crie um programa que leia vários números inteiros pelo teclado.
   O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
   No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag 999)'''

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
