'''Faça um programa que leia um numero de 0 - 9999 e mostre na tela cada um dos digitos separados.
   ex: digite um numero: 1234
   ex: unidade: 4, dezena: 3, centena: 2, milhar: 1.'''

n1 = int(input('digite um numero de 0 ate 9999: '))
unidade = n1//1 % 10
dezena = n1//10 % 10
centena = n1//100 % 10
milhar = n1//1000
print('unidade',unidade)
print('dezena',dezena)
print('centena',centena)
print('milhar',milhar)

n1 = input('digite um numero ate 9999: ')
print(n1[0])
print(n1[1])
print(n1[2])
print(n1[3])
