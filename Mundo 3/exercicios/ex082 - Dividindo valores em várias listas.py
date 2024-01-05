'''Crie um programa que vai ler vários números e colocar em uma lista.
   Depois disso, Crie duas listas extras que vão conter apenas os valores
   pares e os valores impares digitados, respectivamente.
   Ao final, mostre o conteudo das três listas geradas.'''

lista = []
par = []
impar = []
while True:
    n1 = int(input('digite um valor: '))
    if n1 % 2 == 0:
        lista.append(n1)
        par.append(n1)
    else:
        lista.append(n1)
        impar.append(n1)
    n2 = input('quer continuar? [S/N]: ')
    if n2 in 'nN':
        break
print(f'a lista completa é {lista}')
print(f'a lista de pares é {par}')
print(f'a lista de impares é {impar}')
