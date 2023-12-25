# contagem regressiva
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('bum')

'''alternativa'''

i = 11
for c in range(1, 11):
    i = i - 1
    print(i)
    sleep(1)
print('bum')
