import os, sys

'''
 Dessa forma, avisamos ao Python que a função open deve ser atribuída à variável arquivo. 
 Repare que não precisamos chamar a função close, porque quando abrimos o arquivo dessa forma o próprio python fecha 
 o arquivo após sairmos do método acima. Repare também que foi usado um modo novo, o "r+". o "+" significa que estamos 
 abrindo o arquivo tanto para leitura como para escrita. Utilizando o "r+" para escrever começaremos a 
 partir da primeira linha e caso exista algo escrito no arquivo, as linhas serão reescritas conforme 
 formos escrevendo. A diferença para o "w+" é que mesmo que reescrevêssemos apenas a primeira linha, 
 todo o arquivo seria reescrito.
'''
#uma maneira diferente de escrever no arquivo.
'''
with open('./tmp/arquivoTeste.txt', 'r+') as arquivo:
    arquivo.write('Essa é primeira linha escrita no arquivo \n')
    arquivo.write('essa é a segunda linha escrita no arquivo.')
    print(arquivo.read())

input('Pressione enter para sair.')
'''

'''
Uma forma de escrever no final do arquivo é abrindo ele no modo "a". Vejamos o exemplo: 
'''

#with open('./tmp/arquivoTeste.txt', 'a+') as arquivo2:

