'''Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor'''

n1 = int(input('digite um numero: '))
suc = n1 + 1
ant = n1 - 1
print('o numero digitado foi {}, seu sucessor é {}, e seu antecessor é {}'.format(n1, suc, ant))

n1 = int(input('digite um numero: '))
print('o numero digitado foi {}, seu sucessor é {}, e seu antecessor é {}'.format(n1, n1+1, n1-1))
