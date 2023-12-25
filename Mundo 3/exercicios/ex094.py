lista = []
temporario = {}
media = 0
mulheres = []
while True:
    temporario['nome'] = str(input('nome: '))
    temporario['idade'] = int(input('idade: '))
    if temporario['idade'] not in range(0, 999):
        while True:
            print('comando errado, digite um valor valido')
            temporario['idade'] = int(input('idade: '))
            if temporario['idade'] in range(1, 999):
                break
    temporario['sexo'] = str(input('sexo [M/F]: '))
    if temporario['sexo'] not in 'MmfF':
        while True:
            print('comando errado, digite um valor valido')
            temporario['sexo'] = str(input('sexo [M/F]: '))
            if temporario['sexo'] in 'mMFf':
                break
    media = media + temporario['idade']
    if temporario['sexo'] in 'fF':
        mulheres.append(temporario['nome'])
    lista.append(temporario.copy())
    temporario.clear()
    n1 = str(input('quer continuar? [S/N]'))
    if n1 not in 'SsnN':
        while True:
            print('comando errado, digite um valor valido')
            n1 = str(input('quer continuar? [S/N]'))
            if n1 in 'SsnN':
                break
    if n1 in 'nN':
        break
print(f'ao todo temos {len(lista)} pessoas cadastradas')
print(f'a media de idade é de {media/len(lista)}')
print(f'as mulheres cadastradas foram {mulheres}')
print('lista das pessoas que estao acima da media')
for c, v in enumerate(lista):
    if lista[c]['idade'] > media/len(lista):
        print(f'nome = , {v}')
