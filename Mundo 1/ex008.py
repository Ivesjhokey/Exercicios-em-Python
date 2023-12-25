metros = int(input('digite um valor em metros: '))
centimetros = metros*100
milimetros = metros*1000
kilometro = metros/1000
hectometro = metros/100
decametro = metros/10
decimetro = metros*10

print('{} metro(s) sao {} centimetro(s) e {} milimetro(s)'.format(metros, centimetros, milimetros))
print('{} metro(s) sao {} kilometros(s) e {} hectometros(s)'.format(metros, kilometro, hectometro))
print('{} metro(s) sao {} decametro(s) e {} decimetro(s)'.format(metros, decametro, decimetro))

