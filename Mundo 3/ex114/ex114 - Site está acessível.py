"""Crie um código em python que teste se o site Pudim está acessível pelo computador usado."""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'o site nao esta acessivel no momento.')
else:
    print('deu tudo certo')
    # print(site.reade()) vai mostrar o codigo do site
    # voce consegue pegar o conteudo html que vc esta tentando acessar
finally:
    print('muito obrigado, tenha um bom dia!')
