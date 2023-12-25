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
