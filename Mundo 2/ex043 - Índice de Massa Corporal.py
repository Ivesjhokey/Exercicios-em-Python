'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu Status, de acordo com a tabela abaixo:
   - Abaixo de 18.5 = abaixo do peso
   - Entre 18.5 e 25.0 = peso ideal
   - Entre 25.0 até 30.0 = sobrepeso
   - Entre 30.0 até 40.0 = obesidade
   - Acima de 40 = obesidade mórbida'''

altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
imc = peso / ((altura / 100) ** 2)
print(imc)
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('peso ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')
