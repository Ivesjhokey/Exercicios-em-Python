'''Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a operacão solicitada em cada caso
   1 - Somar
   2 - Multiplicar
   3 - Maior
   4 - Novos numeros
   5 - Sair do programa'''

# alternativa 1 jhokey

n1 = float(input('digite um valor: '))
n2 = float(input('digite outro valor: '))
c1 = 1
while c1 != 0:
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
    c2 = int(input('escolha uma operação: '))
    if c2 == 5:
        c1 = c1 - 1
    elif c2 == 4:
        n1 = float(input('digite um valor: '))
        n2 = float(input('digite outro valor: '))
    elif c2 == 3:
        if n1 > n2:
            print(n1,'é o maior')
        else:
            print(n2,'é o maior')
    elif c2 == 2:
        print(n1 * n2)
    elif c2 == 1:
        print(n1 + n2)
    else:
        print('opeção invalida, tente novamente')
print('fim')

# alternativa 2 jhokey

n1 = float(input('digite um valor: '))
n2 = float(input('digite outro valor: '))
c1 = 1
while c1 != 0:
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
    c1 = int(input('escolha uma operação: '))
    if c1 == 5:
        c1 = 0
    elif c1 == 4:
        n1 = float(input('digite um valor: '))
        n2 = float(input('digite outro valor: '))
    elif c1 == 3:
        if n1 > n2:
            print(n1,'é o maior')
        else:
            print(n2,'é o maior')
    elif c1 == 2:
        print(n1 * n2)
    elif c1 == 1:
        print(n1 + n2)
    else:
        print('opeção invalida, tente novamente')
print('fim')