import os, sys

#input('Id do programa e o diretorio de trabalho')
#print(os.getpid(), os.getcwd())


escreveAqr = input('Deseja criar o arquivo? [s/n]').lower()

if escreveAqr == 's':
    if os.path.exists('./tmp') != True:
       os.makedirs('./tmp/')
    #alterar as opções na abertura do arquivo para testes.  'a+', 'w+', 'r+', 'w', 'r', 'a'.
    arquivo = open('./tmp/arquivoTeste.txt', 'w+', encoding='UTF-8')
    arquivo.write('Essa é primeira linha escrita no arquivo \n')
    arquivo.write('essa é a segunda linha escrita no arquivo.')
    arquivo.write('essa deveria ser a terceira linha porém ainda é a segunda pela falta do BARRA N. \n')
    arquivo.write('essa sim é a terceira linha do arquivo.')

    arquivo.close()
else:
    print('Não foi informado um arquivo!')
    input('Pressione enter para sair.')


#os.makedirs('./tmp')