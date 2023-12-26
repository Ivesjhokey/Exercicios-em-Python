'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços'''

for c in range(1, 3):
    n1 = input('digite uma frase: ')
    n1 = n1.split()
    n1 = ''.join(n1)
    n2 = n1[::-1]
    if n1 == n2:
        print('é um palindromo')
    else:
        print('nao é um palindromo')

# alternativa guanabara

frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('nao temos um palindromo')
