'''Escreva um Programa que converta uma temperatura digitada em Celsius e converta para fahrenheit'''

celcius = int(input('digite um valor em celcius: '))
fahrenheit = (celcius * 9/5) + 32
print('{}° celcius sao {}° fahrenheit'.format(celcius, fahrenheit))
