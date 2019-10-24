'''

 Praticar...

'''
from time import sleep

import os, sys

arqBusca = "CN02_CT02.txt"
arquivo = open('./tmp/CN02_CT02.txt', 'r')
#print(arquivo.read())
cont = 0
arquivoFiltrado = []
idd = 0
for linha in arquivo.readlines():
    cont += 1
    if 'Mensagem recebida na entrada do conector.' in linha:
        posicao = linha.split('ID:<')
        idd = posicao[1][0:5]
        print(cont, linha)
        print(posicao)
        print(idd)
    if idd in linha:
        arquivoFiltrado.append(linha)

arquivo.close()




