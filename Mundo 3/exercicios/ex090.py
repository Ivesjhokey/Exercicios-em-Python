# alternativa 1 jhokey
temp = {'nome': str(input('qual o nome? ')), 'media': float(input('qual a media? '))}
print(f'nome = {temp["nome"]}\nmedia = {temp["media"]}\nsituação = {"aprovado" if temp["media"] > 7 else "reprovado"}')

# alternativa guanabara

temp = {}
temp['nome'] = str(input('qual o nome? '))
temp['media'] = float(input('qual a media? '))
if temp['media'] >= 6:
    temp['situação'] = 'aprovado'
elif 5 <= temp['media'] < 6:
    temp['situação'] = 'recuperação'
else:
    temp['situação'] = 'reprovado'
print(f'{temp["nome"]} = {temp["situação"]}')
