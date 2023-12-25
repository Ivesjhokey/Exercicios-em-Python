'''Faça um programa quie leia algo pelo teclado e mostre na tela
   o seu tipo primitivo e todas as informaçoes possiveis sobre ele'''


a1 = input('digie algo: ')
print('o tipo primitivo dese valor é ',type(a1))
print('é numerico?', a1.isnumeric())
print('é alfabetico?', a1.isalpha())
print('é alfanumerico?', a1.isalnum())
print('é um ASCII?', a1.isascii())
print('é digito?', a1.isdigit())
print('é tudo minusculo?', a1.islower())
print('é decimal?', a1.isdecimal())
print('é um identificador', a1.isidentifier())
print('é imprimivel?', a1.isprintable())
print('so tem espaços?', a1.isspace())
print('é tudo maiusculo?', a1.isupper())
print('esta capitalizada?', a1.istitle())
print(a1.__init_subclass__())
if a1.isidentifier:(print('é um identificador'))
