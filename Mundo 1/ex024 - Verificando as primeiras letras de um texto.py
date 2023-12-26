'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.'''

cidade = input('digite o nome da cidade: ').strip().lower()
cidade = cidade.split()

print('santo' in cidade[0])
print(cidade[0:5] == 'santo')
