'''Crie um programa onde o usuário possa digitar varios valores numéricos
   e cadastre-os em uma lista. Caso o numero ja exista lá dentro, ele não
   será adicionado. No final, serão exibidos todos os valores únicos
   digitados, em ordem crescente'''

#alternativa Jhokey
lista = []

while True:
    n1 = int(input('digite um valor: '))
    if n1 in lista:
        print('valor duplicado, nao sera adicionado.')
    else:
        lista.append(n1)
    n2 = input('quer continuar? S/N ')
    if n2 in 'nN':
        break
lista.sort()
print(f'voce digitou os valores {lista}')

#Alternativa Guanabara
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('o Valor foi adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')
