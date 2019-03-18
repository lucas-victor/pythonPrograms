import os, sys

#adiciona novas linhas ao final do arquivo.   opção:   a+
arquivo = open('./tmp/arquivoTeste2.txt', 'a+')

arquivo.write('adicionando linhas novas no arquivo. \n')
arquivo.write('segunda linha do arquivo \n')
arquivo.write('terceira linha do arquivo.\n')
arquivo.close()


#abre o arquivo somente para leitura. opção:   r
arquivo = open('./tmp/arquivoTeste2.txt', 'r')
print(arquivo.read())
arquivo.close()

#input()


#apaga o conteúdo do arquivo para adicionar as linhas novas opção:   w+
'''Se tentarmos abrir um arquivo para escrita que não existe, 
então ele será criado, porém, se ele já existir, 
todo seu conteúdo será apagado no momento em que abrimos o arquivo.'''

'''
arquivo = open('./tmp/arquivoTeste2.txt', 'w+')
arquivo.write('teste apagando arquivo com w+ ')
print(arquivo.read())
arquivo.close()
print()
'''
input('pressione enter para sair.')
