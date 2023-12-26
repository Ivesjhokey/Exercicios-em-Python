'''Crie um programa que leia vários números inteiros pelo teclado. O programa so vai parar quando o usuário digitar o valor 999, que é a condição de parada.
   No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag)'''

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
