'''Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
   Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
   foram nescessários para vencer'''

# alternativa 1 jhokey
from random import randint

c1 = 1
erros = 0
while c1 != 0:
    print('acerte o numero da sorte que o computador esta pensando de 1 - 5.')
    n1 = int(input('digite um numero: '))
    n2 = randint(1, 5)
    if n1 == n2:
        print('o numero da sorte é {}, parabéns!'.format(n2))
        c1 = c1 - 1
    else:
        print('voce errou!')
        erros = erros + 1

print('voce errou {} vezes'.format(erros))

# alternativa 2 jhokey

from random import randint

print('acerte o numero da sorte que o computador esta pensando de 1 - 10.')
n1 = int(input('digite um numero: '))
n2 = randint(1, 10)
erros = 0
while n1 != n2:
    if n1 < n2:
        n1 = int(input('um pouco mais'))
    elif n1 > n2:
        n1 = int(input('um pouco menos'))
    erros = erros + 1
if n1 == n2:
    print('o numero da sorte é {}, parabéns!'.format(n2))
print('voce errou {} vezes'.format(erros))

# alternativa jhokey 3

from random import randint

print('acerte o numero da sorte que o computador esta pensando de 1 - 10.')
n2 = randint(1, 10)
tentativas = 0
acertou = False
while not acertou:  # enquanto nao acertou, ou enquanto acertou nao for verdadeiro faça isso
    tentativas += 1
    n1 = int(input('digite um numero: '))
    if n1 < n2:
        print('um pouco mais')
    elif n1 > n2:
        print('um pouco menos')
    elif n1 == n2:
        print('o numero da sorte é {}, parabéns!'.format(n2))
        acertou = True
print('voce acertou com {} tentativas, parabens'.format(tentativas))

# alternativa guanabara

from random import randint

print('acerte o numero da sorte que o computador esta pensando de 1 - 10.')
n2 = randint(1, 10)
tentativas = 0
acertou = False
while not acertou:  # enquanto nao acertou, ou enquanto acertou nao for verdadeiro faça isso
    n1 = int(input('digite um numero: '))
    tentativas += 1
    if n1 == n2:
        acertou = True
    else:
        if n1 < n2:
            print('um pouco mais')
        elif n1 > n2:
            print('um pouco menos')
print('voce acertou com {} tentativas, parabens'.format(tentativas))
