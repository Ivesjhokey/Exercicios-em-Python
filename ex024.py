cidade = input('digite o nome da cidade: ').strip().lower()
cidade = cidade.split()

print('santo' in cidade[0])
print(cidade[0:5] == 'santo')
