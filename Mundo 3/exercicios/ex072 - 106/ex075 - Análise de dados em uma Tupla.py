'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
   no final, mostre:
   A - Quantas vezes apareceu o valor 9
   B - Em que posição foi digitado o primeiro valor 3
   C - Quais foram os números pares'''

n1 = int(input('digite um valor: '))
n2 = int(input('digite um valor: '))
n3 = int(input('digite um valor: '))
n4 = int(input('digite um valor: '))
n5 = (n1, n2, n3, n4)
print(n5)
print(n5.count(9))
if 3 in n5:
    print(n5.index(3))
else:
    print('nao possui o numero 3')

print(f'os numeros pares foram: ', end=' ')
for c in range(0, len(n5)):
    if (n5[c]) % 2 == 0:
        print(f'{n5[c]} ', end=' ')
