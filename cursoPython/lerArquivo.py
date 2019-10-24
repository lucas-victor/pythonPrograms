import os
import sys


lerArq = input('Deseja ler o arquivo da pasta tmp? [s/n]').lower()


if lerArq == 's':
    if os.path.exists('./tmp') != True:
       os.makedirs('./tmp/')
    arquivo = open('./tmp/arquivoTeste.txt', 'r')
    arqLido = arquivo.read()
    print(arqLido)
    pathDividido = arquivo.name.split('/')
    divisoes = len(pathDividido)
    nomeArqLido = pathDividido[divisoes - 1]
    print(f'Arquivo lido: {nomeArqLido}\n')
    arquivo.close()

    criaCopia = input('Deseja fazer uma cópia do arquivo? [s/n]').lower()
    if criaCopia == 's':
#        if os.path.exists('./tmp/arquivoCriadoWrited.txt') != True:
#            os.makedirs('./tmp/arquivoCriadoWrited.txt')
        arquivoWrited = open('./tmp/arquivoTeste4.txt', 'w', encoding='UTF-8')
        arquivoWrited.write(arqLido)
        arquivoWrited.close()
        print(f'Arquivo copiado em: {arquivoWrited.name}')
else:
    input('Não será lido nenhuma arquivo! Pressione enter para sair.')


