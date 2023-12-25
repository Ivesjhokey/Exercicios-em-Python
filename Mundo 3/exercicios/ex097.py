def escreva(msg):
    texto = len(msg)
    print('~' * (texto + 4))    # print('~' * len(msg + 4))
    print(f'  {msg}')
    print('~' * (texto + 4))    # print('~' * len(msg + 4))


escreva('ives santana')
escreva('pirocudo')
escreva('ives santana pirocudo')
