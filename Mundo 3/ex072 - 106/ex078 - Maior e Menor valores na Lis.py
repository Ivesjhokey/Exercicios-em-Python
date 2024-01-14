'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
   No final, mostre qual foi o maior e o menor valor digitado e as suas
   respectivas posiçôes na lista.'''

# alternativa jhokey
num = []
mai = 0
men = 0

for c in range (0, 5):
    num.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = num[c]
    elif num[c] > mai:
        mai = num[c]
    elif num[c] < men:
        men = num[c]

print(f'o maior valor é {mai}, e esta nas posições: ',end='')
for c in range(0, len(num)):
    if num[c] == mai:
        print(f'{c}... ',end='')
print()
print(f'o menor valor é {men}, e esta nas posições: ',end='')
for c in range(0, len(num)):
    if num[c] == men:
        print(f'{c}... ',end='')


#alternativa guanabara
listanum = []
mai = 0
men = 0

for c in range (0, 5):
    listanum.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'o maior valor digitado foi {mai}, nas posiçoes ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ',end='')
print()

print(f'o menor valor digitado foi {men}, nas posiçoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ',end='')
print()
