import os, sys

lerArq = input('deseja ler o arquivo da pasta tmp? [s/n]').lower()

if lerArq == 's':
    arquivo = open('./tmp/arquivoTeste.txt', 'r')
    print(arquivo.read())
    arquivo.close()
else:
    input('Não será lido nenhuma arquivo! Pressione enter para sair.')