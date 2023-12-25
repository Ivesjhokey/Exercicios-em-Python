#alternativa 1 jhokey

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n1 = int(input('digite um numero de 0 a 20: '))
    if n1 <= 20 and n1 >= 0:
        for c, cont in enumerate(numeros):
            if n1 == c:
                print(f'voce escreveu o numero {cont}')
                break
        break
    else:
        print('tente novamente.', end=' ')

# alternativa 2 jhokey

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n1 = int(input('digite um numero de 0 a 20: '))
    if 20 >= n1 >= 0:
        print(f'voce escreveu o numero {numeros[n1]}')
        break
    else:
        print('tente novamente.', end=' ')
