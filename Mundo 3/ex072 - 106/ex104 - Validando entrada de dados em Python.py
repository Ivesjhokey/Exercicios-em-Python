'''Crie um programa que tenha a função leiaInt(), que vai funcionar
   de forma semelhante a função input() do Python só que fazendo
   a validação para aceitar apenas um valor numérico
   Ex: n = leiaInt('Digite um n: ')'''

def leiaint(a):
    a = input(a)
    if a.isnumeric():
        a = int(a)
        return f'voce digitou o numero {a}'
    else:
        return 'voce nao digitou um numero'

n = leiaint('digite um numero: ')
print(n)
