'''Crie um programa que vai ler vários números e colocar em uma lista.
   Depois disso, mostre:
   A: Quantos números foram digitados
   B: A lista de valores, ordenada de forma decrescente
   C: Se o valor 5 foi digitado e está ou não na lista'''

#Alternativa 1 jhokey
lista = []
while True:
    lista.append(int(input('digite um valor: ')))
    n1 = input('quer continuar? [S/N]: ')
    if n1 in 'nN':
        break
print(f'foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 nao faz parte da lista')

#aternativa 2 jhokey
lista = []
while True:
    n1 = int(input('digite um valor: '))
    if len(lista) == 0 or n1 >= lista[0]:
        lista.insert(0, n1)
    else:
        pos = 0
        while pos < len(lista):
            if n1 >= lista[pos]:
                lista.insert(pos, n1)
                pos += 1
                break
            else:
                lista.append(n1)
                pos += 1
                break
    n2 = input('quer continuar? [S/N]: ')
    if n2 in 'nN':
        break
print(f'foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 nao faz parte da lista')
