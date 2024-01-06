'''Faça um programa que tenha uma função chamada escreva(), que
   receba um texto qualquer como parâmetro e mostre uma mensagem
   com tamanho adaptavel.
   EX: escreva('Ola,Mundo!')
   SAIDA : ~~~~~~~~~~~~
            Olá,Mundo!
           ~~~~~~~~~~~~'''

def escreva(msg):
    texto = len(msg)
    print('~' * (texto + 4))    # print('~' * len(msg + 4))
    print(f'  {msg}')
    print('~' * (texto + 4))    # print('~' * len(msg + 4))


escreva('ives santana')
escreva('pirocudo')
escreva('ives santana pirocudo')
