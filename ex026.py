frase = input('digite uma frase: ').strip().upper()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a letra A aparece pela primeira vez na posição {}'.format(frase.find('A')))
print('a letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A')))
