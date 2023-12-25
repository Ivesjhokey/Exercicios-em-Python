from random import randint

print('acerte o numero da sorte que o computador esta pensando de 1 - 5.')
n1 = int(input('digite um numero: '))
n2 = randint(1, 5)

if n1 == n2:
    print('o numero da sorte é {}, parabéns!'.format(n2))
else:
    print('voce errou!')
