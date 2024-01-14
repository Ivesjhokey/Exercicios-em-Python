'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
   na ordem de colocação. Depois mostre:
   A - Os 5 primeiros
   B - Os ultimos 4 colocados
   C - Times em ordem alfabética
   D - Em que posição esta o time do corinthians'''

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense',
         'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América Fc Saf', 'Botafogo', 'Santos', 'Goiás',
         'Red Bull Bragantino', 'Coritiba', 'Cuiabá Saf', 'Ceará', 'Atlético', 'Avaí', 'Juventude')
print(len(times))
print(times[0:5])
print(times[:2:-1])
print(sorted(times))
print(times.index('Corinthians')+1)
