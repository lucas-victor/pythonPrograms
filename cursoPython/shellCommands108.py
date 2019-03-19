import os


os.system('touch arquivoTeste.txt')
os.system('echo "escrevendo no arquivo para usar o cat por comando" > arquivoTeste.txt')
catArq = os.system('cat arquivoTeste.txt')
#lembrando que o retorno do os.system é sempre o valor 0 para sucesso ou != 0 para falhas.
print('Retorno do cat no arquivoTeste.txt, sucesso(0) ou falha(!=0)', catArq)

input('Criado o arq, escrito nele com echo, e dado o cat no arquivo. \n Pressione enter para continuar.')

#executa o comando no linux e guarda o retorno
textArq = os.popen('cat arquivoTeste.txt').read()
print('Exibe o retorno do comando executado, no caso "(cat arquivoTeste.txt).read()". \n', textArq)

#executa o comando no linux e guarda o retorno em uma lista. cada linha em um item da lista.
textArq2 = os.popen('cat arquivoTeste.txt').readlines()
print('Exibe o retorno do comando executado, gerando uma lista com cada linha. "(cat arquivoTeste.txt).read()" \n', textArq2)






