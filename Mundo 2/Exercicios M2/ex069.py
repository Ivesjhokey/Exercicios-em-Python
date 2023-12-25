cont = homem = mulher18 = pessoa18 = 0
while True:
    print('CADASTRE UMA PESSOA')
    n1 = int(input('qual sua idade?: '))
    n2 = input('qual seu sexo?[F/M]: ').upper()
    cont += 1
    if n1 < 20 and n2 == 'F':
        mulher18 += 1
        if n1 > 18:
            pessoa18 += 1
    elif n1 > 18:
        pessoa18 += 1
    if n2 == 'M':
        homem += 1
    n3 = input('quer continuar?[S/N]: ').upper()
    if n3 == 'N':
        break
print(f'ao todo foram cadastradas {cont} pessoas, {mulher18} mulheres com menos de 20 anos,'
      f' {pessoa18} pessoas com mais de 18 anos, e {homem} homens')
